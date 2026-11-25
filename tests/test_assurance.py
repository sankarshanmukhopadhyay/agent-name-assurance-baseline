import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from jsonschema import ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import validate_a2a_assurance as gate
import validate_implementation_fixtures as fixtures


class GateTests(unittest.TestCase):
    def setUp(self):
        self.vector = json.loads((gate.VECTORS / "valid-verified-agent.json").read_text())

    def test_schema_required(self):
        del self.vector["extension"]["params"]["cardBinding"]["issuer"]
        self.assertEqual(gate.evaluate(self.vector), "deny-invalid-extension")

    def test_expiry_boundary(self):
        self.vector["extension"]["params"]["freshness"]["expiresAt"] = self.vector["evaluated_at"]
        self.assertEqual(gate.evaluate(self.vector), "deny-stale")

    def test_cache_only(self):
        freshness = self.vector["extension"]["params"]["freshness"]
        del freshness["expiresAt"]
        freshness["maxCacheAgeSeconds"] = 86400
        self.assertEqual(gate.evaluate(self.vector), "allow-assurance-evaluation")
        freshness["maxCacheAgeSeconds"] = 86399
        self.assertEqual(gate.evaluate(self.vector), "deny-stale")

    def test_boolean_spoof(self):
        self.vector["consequential"] = "false"
        self.assertEqual(gate.evaluate(self.vector), "deny-invalid-input")

    def test_required_absent(self):
        self.vector["extension"] = None
        self.vector["anab_required"] = True
        self.assertEqual(gate.evaluate(self.vector), "deny-missing-required-extension")

    def test_empty_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / "manifest.json").write_text('{"vectors":[]}')
            with patch.object(gate, "VECTORS", path), self.assertRaises(ValueError):
                gate.run()


class FixtureTests(unittest.TestCase):
    def setUp(self):
        self.case = json.loads((fixtures.PACK / "cases/ANAB-FX-001.json").read_text())

    def normalize(self):
        return fixtures.normalize(json.dumps(self.case).encode())

    def test_no_expected_outcome_in_input(self):
        doc = self.normalize()
        self.assertNotIn("expected_outcome", json.dumps(doc))
        self.case["expected_outcome"] = "PASS"
        with self.assertRaises(ValidationError):
            self.normalize()

    def test_empty_bindings(self):
        self.case["requirement_evidence"] = {}
        with self.assertRaises(ValidationError):
            self.normalize()

    def test_duplicate_observation(self):
        self.case["observations"].append(copy.deepcopy(self.case["observations"][0]))
        with self.assertRaises(ValueError):
            self.normalize()

    def test_unbound_observation(self):
        self.case["observations"].append({"id":"extra","status":"available","description":"unbound",
                                          "observation_ref":"urn:extra"})
        with self.assertRaises(ValueError):
            self.normalize()

    def test_absent_observation(self):
        self.case["observations"].pop()
        with self.assertRaises(ValueError):
            self.normalize()

    def test_invalid_time(self):
        self.case["evaluation_time"] = "yesterday"
        with self.assertRaises(ValidationError):
            self.normalize()

    def test_policy_cannot_force_pass(self):
        self.case["policy"]["stale_evidence"] = "PASS"
        with self.assertRaises(ValidationError):
            self.normalize()

    def test_duplicate_json_key(self):
        with self.assertRaises(ValueError):
            fixtures.load(b'{"a":1,"a":2}')

    def test_manifest_controls_and_nonvacuity(self):
        with tempfile.TemporaryDirectory() as directory:
            pack = Path(directory) / "fixtures"
            shutil.copytree(fixtures.PACK, pack)
            path = pack / "implementation-validation-manifest.json"
            manifest = json.loads(path.read_text())
            manifest["fixtures"][0]["requirements"].append("ANAGB-FAKE-99")
            path.write_text(json.dumps(manifest))
            with self.assertRaises(ValueError):
                fixtures.validate_pack(pack)
            manifest["fixtures"] = []
            path.write_text(json.dumps(manifest))
            with self.assertRaises(ValidationError):
                fixtures.validate_pack(pack)

    def test_fixture_pack(self):
        _, cases = fixtures.validate_pack()
        self.assertEqual(len(cases), 6)


if __name__ == "__main__":
    unittest.main()

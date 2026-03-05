# Agent Names and Agent Pages (working extract)

This file is a **non-normative working extract** created from the upstream draft shared with this repository.

- **Upstream title:** Agent Names and Agent Pages
- **Upstream version:** 2026-02-07—V5
- **Provenance:** Extracted from the source `.docx` provided to this repo (for review and control-mapping).
- **Extraction date:** 2026-03-05

---

Agent Names and Agent Pages

2026-02-07—V5

This is a proposal for submission to the ToIP / DIF Decentralized Trust Graph Working Group (DTGWG) based on early work in the First Person Project on human-friendly naming and discovery for decentralized identifiers (DIDs).

TERMINOLOGY NOTE:Tterms used in this document are defined in the DTG Glossary. Terms in bold in this document we propose to add to the DTG Glossary.

BACKGROUND READING: This document assumes the reader is familiar with decentralized identifiers (DIDs) and verifiable credentials (VCs). For more information on both, see Part 3 of the First Person Project white paper.

CONTENTS

What is an agent name?

Decentralized identifiers (DIDs) must be both globally unique and secure, so as identifiers, they can’t cover the third point of Zooko’s Triangle: human memorability.

DIDs are basically long strings of numbers and digits that nobody can remember—they must take that form in order to be both decentralized (not requiring any centralized registry) and cryptographically verifiable (so the owner can prove control). Therefore, to make DIDs easy for people to use, it can be very helpful to layer a simple naming system over them just like DNS names were layered over IP addresses.

Why are they called agent names?

This new form of digital address is called an agent name because: a) the proposed syntax is based on the “@name” convention used in social media, and b) the network endpoint identified by the address is called a verifiable trust agent (VTA). Please see the DTG Glossary and the VTC Bootstrapping document for a more complete description of a VTA.

What does an agent name look like?

Any globally resolvable human-memorable naming system cannot be fully decentralized. We propose the next best thing: taking the “@name” convention widely established in social media (Twitter/X, Slack, Teams, Bluesky, etc.) and prefixing the @name with a domain name. The resulting character string looks very similar to an email address. Also, like an email address, it is globally unique. However, unlike an email address, this string is also a resolvable URL. Examples:

example.com/@alice

connect.me/@bob

names.somewhere.info/@john-smith

anydomain.io/@any.name.can.go.here

anydomain.io/@an-agent-name/can/include/paths

Can an agent name be contextualized by including a path?

Yes. One of the benefits of agent name syntax is that it is as flexible as URL path syntax. For example, a person attending an event can simply append the event name to the agent name (or names) they wish to share at that event. Example:

firstperson.network/@drummond/h2hsummit

Now a contact request resulting from that agent name can be recognized as originating from that context.

See also the answer to this question: Is there a standard syntax for representing specific VTA capabilities?

Why is an agent name machine-recognizeable?

An agent name string is a URL that follows one rule: the path component must begin with an @sign. This “slash at” (“/@”) syntax makes an agent name string easy for both humans and machines to recognize.

What is an agent name parser?

Just like parsers that detect if a text string contains an email address or a URL (thus automatically turning it into a clickable link), an agent name parser can detect if a text string contains an agent name. If so, the parser can invoke an agent name resolver.

What is an agent name resolver?

An agent name resolver resolves the agent name to a DID (typically through a simple web redirect). Then the ​​agent name resolver calls a DID resolver to resolve the DID to a DID document that provides the public key(s) and network endpoint(s) for the target verifiable trust agent (VTA). The party clicking the link can then request a First Person connection (or other agent-enabled interaction) with the VTA.

Who can host an agent name service?

As these examples illustrate, an agent name can be hosted at any domain and use any syntax allowable in a URL. So agent name service is essentially hosting a web service redirecting a URL to a DID—and in most cases serving up the associated DID document.

However, in addition to agent name hosting, a full-service agent name service provider will typically offer three other services:

Agent name registration.

Agent name verification.

Agent page hosting.

Note that all of these services—along with VTA hosting—may also be offered by a verifiable trust service provider (VTSP).

What is agent name registration?

Since an agent name needs to be resolvable on the Web, a web server must be configured to respond with the appropriate redirect (and potentially with the DID document if: a) the agent name resolves to a web-based DID method such as did:webvh, and b) the DID document is stored on that same web server).

This configuration can be done manually by a web-savvy developer who has access to the web server. Alternatively, the process be automated using a client application such as a personal network manager (PNM—as discussed in the First Person Project white paper) that calls an API offered by an agent name service provider.

What is an agent page?

An agent name can resolve to any digital resource. However, when an agent name resolves to a human- and machine-readable interface for a VTA, that is called an agent page. All four types of DTG nodes can have agent pages:

People. In the First Person Project white paper, these are called First Person Pages.

Verifiable trust communities (VTCs). This is the DTG Glossary term for any group or organization of any size or kind.

Devices. The agent page for a device is one way a person or a VTC can “pair” with that device (smartphone, laptop, desktop, server, smart car, etc.) to add it to their personal or community trust network.

AI agents. The agent page for an AI agent is one way a person or VTC can pair with it. See this question: Can an independent AI agent have an agent name?

Agent pages are designed to be consumed in either of two modes: 1) browser view, or 2) agent view.

What is the browser view of an agent page?

If an agent page is viewed in a browser that is not agent-enabled, it will appear as an ordinary web page that can contain any standard web content. This page can also contain machine-readable content that is rendered and presented in a human-friendly way, including DTG credentials, content credentials, or other structured data that a DTG node wants to be publicly accessible.

All content on an agent page can be cryptographically verifiable (signed by the DTG node’s keys), and can therefore be linked to and secured by DTG credentials, especially those verifiable by a verifiable trust network (VTN) such as the First Person Network.

How can a human viewer of an agent page learn about agent view?

The agent page can also contain (or link to) human-readable instructions for how to access it in agent view. These instructions will typically advise the reader to: a) add a personal agent extension to their browser, or b) visit the agent page with a personal agent app (e.g., mobile app, desktop app, or web app) such as a personal network manager.

In the case such applications are already installed, the agent page can also trigger the execution of trust tasks in those applications. For example, a button (or QR code) on the agent page can invoke a personal network manager in order to establish a trust relationship, or process a VTC invitation credential.

What is the agent view of an agent page?

When a requesting agent accesses an agent page, it “sees” the associated DID document and other machine-readable content (e.g. DTG credentials) “behind” the human-readable web page. The requesting agent can then discover the agent service endpoint in the DID document and access it to discover a machine-readable description of the target VTA capabilities (similar to agent.md for AI agents). The requesting agent can then negotiate interaction options with the VTA.

What is an example of this type of agent-mediated interaction?

A simple example is contact mediation, where any request to contact the agent owner is mediated by the VTA in order to apply the agent owner’s contact policies. Contact mediation is ideal for anyone who wants a digital address they can publish anywhere on the web or in social media without any worry about spam, e.g., bloggers, social media users, researchers, academics, job seekers, government officials, etc.

How does contact mediation work?

First, the agent owner uses a personal network manager to generate a DID, register an agent name, and set up their agent page. In this last step, the agent owner chooses the contact policies they want their verifiable trust agent to enforce. For example: “Only forward me a contact request if the requestor can prove at least one of the following:”

They can prove ownership of one or more specified social media accounts.

They are a member of the First Person Network.

They are a member of the First Person Cooperative (i.e., they have a First Person Card).

They are a member of another verifiable trust community (or verifiable trust network) the agent owner trusts.

They have a relationship with someone I already have a First Person relationship with.

Can contact mediation policies be more sophisticated?

Yes. They can enforce any kind of authorization policy supported by the VTA’s policy engine. For example, the agent owner could have a policy requiring that the requestor share their own agent name(s) and agent page(s). The owner’s agent can then automatically verify those agent names and pages are authentic (see agent name verification) before forwarding the contact request to the owner. The owner can then preview the requestors own agent page(s) before deciding whether to answer the contact request.

An agent owner could also have a policy enforcing private introductions, i.e., “Only forward contact requests that come through one of my existing First Person trust relationships.”

A sophisticated VTA could even call an AI agent to analyze a contact request and help determine its relevance and priority for the agent owner.

How can an agent name be protected from spoofing attacks?

Since an agent name is not itself a DID, it cannot be directly protected using cryptography. This means it could be as vulnerable to spoofing and phishing attacks as any other URL or email address.

However, there are two levels of defense against such attacks:

AKA verification.

Agent name verification.

What is AKA verification?

When an agent name resolver resolves an agent name, the resolver can automatically verify that the resolved DID document includes an alsoKnownAs entry that includes the agent name URL. If not, the parser can immediately flag the agent name as unauthorized.

However, alsoKnownAs entries in a DID document do not provide protection if the DID document itself is compromised (e.g., via DNS poisoning or a web server breach). For that reason, a second level of defense is needed to provide full cryptographic protection.

What is agent name verification?

The second level of defense is an agent name verification protocol. This is a trust task to be standardized by the DTGWG. The requesting agent can execute this protocol immediately after completing the agent name resolution process in order to verify the authenticity of the agent name before proceeding any further.

The protocol is very simple: the requesting agent requests a standard agent name proof from either: a) the web server hosting the DID document (as described in the Whois section of the Webvh specification), or b) the VTA endpoint listed in the DID document. The response is a presentation of an agent name credential: a verifiable credential (also standardized by the DTGWG) containing the agent name and a nonce.

An agent name credential will typically be issued by an agent name service provider that is recognized within a verifiable trust network (VTN) such as the First Person Network. (See the DTG Glossary and the First Person Project white paper for more about VTNs.)

If: a) the agent name proof verifies against a public key in the DID document, and b) the agent name credential issuer is trusted by the requesting agent, it provides cryptographic proof of control of the agent name that cannot be spoofed without actual control of the private key.

Is there a preferred DID method for agent names?

In theory, an agent name can work with any DID method because it simply redirects to a DID. However a did:scid method, such as did:scid:vh (for the Webvh method)  is preferred because it provides both the strong security and maximum portability provided by self-certifying identifiers (SCIDs).

In addition, the same repository for the did:scid verifiable history data—such as the web server hosting an agent name—can optionally host a decentralized “whois” service for associated public verifiable credentials or other public profile information such as an agent page. See the Webvh specification for more about this whois functionality.

Can agent names be compatible with @names in existing social media or chat apps?

Yes. The developers of existing apps or networks can treat those existing @names as local agent names. That means that resolution of those @names will take place automatically within the context of that app or network (exactly as they do today—no changes needed). Then, if the provider adds support for global agent names as described in this document, i.e., that include the full “/@” syntax, now app or network can then begin to recognize and process agent names that work across all social media apps and sites.

Can a verifiable trust community (VTC) have an agent name?

Yes! VTC agent names use exactly the same syntax—only without adding any path except the @ sign. Examples:

example.com/@

connect.me/@

firstperson.network/@

An agent name that ends with a “/@” will connect with a community VTA.

Can an independent AI agent have an agent name?

Yes. A person or a VTC can give an agent name to an AI agent that has its own “agenthood”, meaning the AI agent can present a DTG VRC proof to prove the AI agent is acting on behalf of a person or a VTC. There does not need to be any difference in agent name syntax. The only difference between an agent name that resolves to a non-AI VTA and an AI-enabled VTA is that the latter will have AI capabilities. (See also the answer to the next question.)

Is there a standard syntax for representing specific VTA capabilities?

Yes. The ToIP Decentralized Trust Graph Working Group can define a dictionary of specific trust task protocols that can be performed with VTAs (including AI VTAs). In this dictionary, each trust task protocol can be identified with a string beginning with “+” sign (much the same way some email service providers enable a “+” sign to be added to an email address to support automatic sorting). Examples:

connect.me/@alice+calendar  ⇐ connects to Alice’s calendar agent

example.com/@+conciege  ⇐ connects to the concierge agent for the example.com VTC.

firstperson.network/@+directory  ⇐ connects to the directory service agent for the firstperson.network VTN.

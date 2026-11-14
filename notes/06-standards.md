# 6. Standards and frameworks: which one to read first

There are many. You don't need all of them. Start from what you're trying to do.

| If you need to… | Read | Cost |
|---|---|---|
| Understand OT security end to end | NIST SP 800-82 Rev. 3 | Free |
| Get a short, prioritized baseline | CISA Cross-Sector Cybersecurity Performance Goals (CPGs) | Free |
| Decide where to spend first | SANS Five ICS Cybersecurity Critical Controls | Free |
| Understand how attackers operate in OT | MITRE ATT&CK for ICS | Free |
| Specify requirements for suppliers and integrators | ISA/IEC 62443 | Paid |
| Fit OT into an existing company security program | NIST Cybersecurity Framework 2.0 | Free |
| Comply as a North American bulk electric utility | NERC CIP | Free, mandatory in scope |

## Notes on each

**NIST SP 800-82 Rev. 3** (2023). The best single free document. It covers OT system types, risk management, architecture and an OT overlay for the NIST SP 800-53 controls. Read the architecture chapter first.

**CISA CPGs.** A short list of high-value practices for IT and OT, written for organizations without a large security team. Good for a first gap assessment and for explaining priorities to management.

**SANS Five Critical Controls.** ICS-specific incident response, defensible architecture, ICS network visibility and monitoring, secure remote access, and risk-based vulnerability management. Useful because it's five things, in order.

**MITRE ATT&CK for ICS.** A catalog of adversary tactics and techniques seen against industrial systems. Use it to check detection coverage and to make sense of incident reports. It's a reference, not a program.

**ISA/IEC 62443.** The international standard series for industrial automation security. Its parts address different audiences:

- 2-1: the asset owner's security program
- 2-4: requirements for integrators and service providers
- 3-2: risk assessment, zones and conduits
- 3-3: system security requirements and security levels (SL 1–4)
- 4-1 and 4-2: product development and component requirements for vendors

As an asset owner you'll use it most when buying: "the system shall meet 62443-3-3 SL 2" is language suppliers understand.

**NIST CSF 2.0.** Not OT-specific, but if the company already reports against it, map OT work into its functions (Govern, Identify, Protect, Detect, Respond, Recover) rather than starting a separate program.

**NERC CIP.** Mandatory for the North American bulk electric system. If you aren't in scope it's still a worked example of enforceable OT requirements.

## A reasonable reading order for a manufacturer

1. CISA CPGs, as a gap checklist (an afternoon)
2. SANS five controls, to set priorities (an hour)
3. NIST SP 800-82 Rev. 3, architecture and risk chapters (a week of evenings)
4. IEC 62443-3-3 and 2-4, when you write your next purchase specification

## Sources

- NIST SP 800-82 Rev. 3: <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- CISA CPGs: <https://www.cisa.gov/cross-sector-cybersecurity-performance-goals>
- SANS Five ICS Cybersecurity Critical Controls: <https://www.sans.org/white-papers/five-ics-cybersecurity-critical-controls/>
- MITRE ATT&CK for ICS: <https://attack.mitre.org/matrices/ics/>
- ISA/IEC 62443 series: <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- NIST Cybersecurity Framework: <https://www.nist.gov/cyberframework>
- NERC CIP standards: <https://www.nerc.com/standards/reliability-standards>

Previous: [5. Remote access](05-remote-access.md) · Next: [7. Incidents worth studying](07-incidents.md)

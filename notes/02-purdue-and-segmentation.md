# 2. The Purdue model and segmentation

Since you often can't patch OT equipment, the main defense is controlling what can talk to it. The Purdue model is the common vocabulary for that. It's a reference model, not a law, and real plants are messier.

## The levels

| Level | Name | Typical equipment |
|---|---|---|
| 5 | Enterprise | Corporate IT, email, internet access |
| 4 | Site business | ERP, file servers, office PCs |
| 3.5 | Industrial DMZ | Jump hosts, patch and antivirus relays, historian replica |
| 3 | Site operations | Historian, MES, engineering workstations, OT domain controllers |
| 2 | Area supervisory | HMIs, SCADA servers |
| 1 | Basic control | PLCs, drives, safety controllers |
| 0 | Process | Sensors, valves, motors |

Levels 0–3 are OT. Levels 4–5 are IT. The line between 3 and 4 is the one that matters most.

## The industrial DMZ (level 3.5)

The rule: **no direct traffic between IT and OT.** Every flow terminates in the DMZ.

- IT users who need production data read a historian replica in the DMZ, not the historian in OT.
- Patches and antivirus updates are staged on a DMZ server and pulled from OT.
- Remote users land on a jump host in the DMZ, then open a second session into OT (see note 5, remote access).
- Default deny in both directions. Each allowed flow has a named owner and a reason.

If you can only afford one project, build this boundary.

## Zones and conduits

IEC 62443 describes the same idea more flexibly. A **zone** is a group of assets with the same security needs. A **conduit** is a controlled path between zones. This fits real plants better than strict levels: a packaging line and a boiler house can be separate zones at the same Purdue level, so a problem in one doesn't spread to the other.

A practical order of work:

1. Separate IT from OT (the DMZ above).
2. Separate safety systems from everything else.
3. Separate production areas or lines from each other.
4. Restrict which workstations can program controllers.

## What goes wrong in practice

- **Flat OT networks.** One big VLAN where every device can reach every other.
- **Dual-homed machines.** An engineering PC with one card in the office network and one in the plant network bypasses the firewall entirely.
- **"Temporary" firewall rules** that allow any-to-any and never get removed.
- **Shared services.** OT machines joined to the corporate Active Directory, so a corporate compromise becomes a plant compromise.
- **Unknown paths.** Cellular modems in vendor cabinets, wireless bridges, remote-support tools left running.
- **Cloud and IIoT** devices that send data straight from level 1 or 2 to the internet. Route these through the DMZ and make them outbound-only.

## Finding out what you have

You can't segment what you can't see. Start passive: a SPAN port or tap on the main OT switches, and a tool that understands industrial protocols, will show the devices and who talks to whom without sending a packet. Use that traffic map to write firewall rules, then run the rules in log-only mode before enforcing them.

## Sources

- NIST SP 800-82 Rev. 3, section on OT network architecture: <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- ISA/IEC 62443 series overview: <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>

Previous: [1. IT vs OT](01-it-vs-ot.md) · Next: [3. Industrial protocols](03-protocols.md)

# 4. Your first 90 days with a plant network

A working order for someone from IT who has just become responsible for OT security. The aim of the first three months is to know what you have, be able to recover it, and close the widest doors. Nothing here needs a large budget.

## Days 1–30: learn and look

Change nothing yet.

- [ ] **Walk the floor** with maintenance or controls engineering. Ask what each line does, what stops it, and what has gone wrong before.
- [ ] **Find the owners.** Who programs the PLCs? Which vendors and integrators have support contracts and remote access?
- [ ] **Collect the drawings** you can find: network diagrams, panel drawings, IP lists. Assume they're out of date.
- [ ] **Build an asset inventory passively.** Switch MAC and ARP tables, DHCP leases, and a capture from a SPAN port. For each device record make, model, firmware, IP, location, function and owner.
- [ ] **List every way in.** IT/OT firewall rules, VPNs, vendor remote-support tools, cellular modems, dual-homed PCs, wireless.
- [ ] **Identify the crown jewels.** Which systems stop production or create a safety risk if they fail? Where are the safety instrumented systems?

## Days 31–60: make it recoverable

Ransomware that reaches OT is a recovery problem. So is a dead engineering laptop.

- [ ] **Back up controller programs and configurations**: PLC, HMI, drive, robot, switch, firewall. Store a copy offline.
- [ ] **Back up the engineering software itself**: installers, license files, project files. A PLC backup is useless if you can't install the software that opens it.
- [ ] **Image the critical PCs**: HMIs, SCADA servers, engineering workstations.
- [ ] **Test one restore.** An untested backup is a guess.
- [ ] **Write a one-page incident plan.** Who can decide to disconnect OT from IT? Who to call at 2 a.m.: plant manager, controls engineer, vendor, insurer? Can the plant run manually, and for how long?
- [ ] **Put the phone list on paper.** The network may be what's down.

## Days 61–90: close the widest doors

Make changes in maintenance windows, agreed with operations, one at a time.

- [ ] **Remote access:** remove always-on vendor connections, require MFA, and route access through a jump host (see [5. Remote access](05-remote-access.md)).
- [ ] **IT/OT boundary:** remove any-to-any rules. Move toward default deny with a DMZ (see [2. The Purdue model and segmentation](02-purdue-and-segmentation.md)).
- [ ] **Internet exposure:** confirm no OT device is reachable from the internet, and that OT machines can't browse it.
- [ ] **Default passwords:** change them on HMIs, switches and remote-access devices where a change won't break an integration. Record where it would.
- [ ] **Shared accounts:** list them. Replace what you can with named accounts, starting with remote access and engineering workstations.
- [ ] **Removable media:** set one rule, such as a scanning station for vendor USB drives.
- [ ] **Passive monitoring:** keep the SPAN capture running, and alert on new devices and on program downloads to controllers.

## Things not to do early

- Run an active vulnerability scanner across the OT network.
- Push corporate GPOs, agents or patch schedules onto OT machines.
- Enforce account lockout or screen-lock timeouts on operator HMIs.
- Replace equipment because it's old. Segment it first.
- Publish a policy before you've met the people it applies to.

## What to tell management at day 90

Keep it to one page: what we have (asset count, unsupported systems), how we'd recover (backup coverage, last restore test), the top five risks in business terms (downtime hours, safety exposure), and the next three projects with rough costs. The CISA Cross-Sector Cybersecurity Performance Goals and the SANS five critical controls both make good yardsticks for that report.

## Sources

- CISA Cross-Sector Cybersecurity Performance Goals: <https://www.cisa.gov/cross-sector-cybersecurity-performance-goals>
- SANS, *The Five ICS Cybersecurity Critical Controls*: <https://www.sans.org/white-papers/five-ics-cybersecurity-critical-controls/>

Previous: [3. Industrial protocols](03-protocols.md) · Next: [5. Remote access](05-remote-access.md)

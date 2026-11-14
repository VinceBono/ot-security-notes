# 1. IT vs OT: what actually changes

Operational technology (OT) is the hardware and software that monitors and controls physical processes: PLCs, drives, HMIs, SCADA servers, safety systems. The security goals sound the same as IT. The priorities and constraints are not.

## Priorities flip

IT security is usually taught as confidentiality, integrity, availability. On a plant floor the order is closer to:

1. **Safety.** Nobody gets hurt, nothing explodes, nothing spills.
2. **Availability.** The process keeps running. Downtime is measured in dollars per minute.
3. **Integrity.** Setpoints, recipes and measurements are correct.
4. **Confidentiality.** Usually last, with exceptions such as recipes and production data.

A control that protects confidentiality at the cost of availability is normally a bad trade in OT.

## The differences that bite

| Topic | IT habit | OT reality |
|---|---|---|
| Patching | Monthly, automated | Needs a planned outage and often vendor approval. Some systems go years between patches |
| Lifespan | 3–5 years | 15–30 years. Unsupported operating systems are common |
| Scanning | Scan everything, often | Active scans have crashed older PLCs and network cards. Start passive |
| Reboots | Cheap fix | A reboot can stop a line or lose a batch |
| Account lockout | Standard | Locking an operator out of an HMI during an upset is a safety problem |
| Antivirus/EDR | Everywhere | May be unsupported by the vendor or interfere with real-time software. Test first |
| Encryption | Default | Many industrial protocols have none, and adding it can break timing or troubleshooting |
| Change control | Ticket and deploy | Changes go through engineering and often a formal management-of-change process |
| Ownership | IT department | Engineering, maintenance and operations own the equipment. Vendors often hold the support contract |

## Why the old stuff is still there

The equipment is not old because someone was lazy. A controller that has run a process reliably for twenty years has no business reason to be replaced, replacing it means re-validating the process, and the software that programs it may only run on an old Windows version. Expect to protect systems you cannot patch. That's what segmentation, monitoring and controlled remote access are for.

## What carries over from IT

Plenty does: asset inventory, least privilege, MFA on remote access, backups you have tested, network segmentation, logging, incident response planning. The skills transfer. The method of applying them changes: slower, tested in a lab or during a shutdown, and agreed with the people who run the process.

## Working with the plant

- **Ask before you touch.** Operations knows what is fragile. You don't yet.
- **Learn the process.** You can't judge risk without knowing what the equipment does physically.
- **Bring something useful.** Backups of PLC programs and a current network drawing win more trust than a policy document.
- **Schedule around production.** Changes happen in maintenance windows, not on Tuesday afternoon.

## Sources

- NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security*: <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- CISA, Industrial Control Systems: <https://www.cisa.gov/topics/industrial-control-systems>

Next: [2. The Purdue model and segmentation](02-purdue-and-segmentation.md)

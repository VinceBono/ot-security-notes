# ot-security-notes

Field notes on OT/ICS security for people who come from IT.

Most security people learn on IT networks, then get handed a plant floor. The instincts that work in IT (scan everything, patch fast, lock accounts, reboot to fix) can stop a production line or hurt someone in OT. These notes cover what changes, what to do first, and where to read more. They're short on purpose: each one is meant to be read in ten minutes.

## Who this is for

- IT directors and sysadmins who just inherited the plant network
- Security analysts moving into industrial work
- Students who want the practical picture before the standards

## Contents

| Note | What it covers |
|---|---|
| [1. IT vs OT](notes/01-it-vs-ot.md) | How priorities, patching, scanning and ownership differ on a plant floor |
| [2. The Purdue model and segmentation](notes/02-purdue-and-segmentation.md) | Levels, the industrial DMZ, zones and conduits, common mistakes |
| [3. Industrial protocols](notes/03-protocols.md) | Modbus, EtherNet/IP, S7, DNP3, OPC UA: ports and what security each has |
| [4. Your first 90 days](notes/04-first-90-days.md) | A checklist: learn and look, make it recoverable, close the widest doors |
| [5. Remote access](notes/05-remote-access.md) | Finding the paths in, a jump-host pattern, rules for vendors |
| [6. Standards and frameworks](notes/06-standards.md) | Which of NIST 800-82, CISA CPGs, IEC 62443 and the rest to read first |
| [7. Incidents worth studying](notes/07-incidents.md) | Stuxnet, Ukraine, TRITON, Oldsmar, Colonial Pipeline and the lesson from each |
| [Resources](resources.md) | Free references, tools for visibility, lab software, books |

## Ground rules

- **Practice on simulators, not production.** Everything here assumes a lab you own. Active scanning and writes to a live controller can trip a process.
- **Nothing here comes from a specific plant.** The notes are general practice and public sources only.
- **Check the date.** Standards and advisories move; each note links to its primary sources so you can confirm.

## Contributing

Corrections and field experience are welcome. Open an issue or a pull request, and cite a public source for factual claims.

## License

Text is [CC BY 4.0](LICENSE). Scripts under `scripts/` are MIT.

# 7. Incidents worth studying

Six public cases, each with the lesson an IT person should take from it. Summaries are short; follow the sources for detail.

## Stuxnet (discovered 2010)

Malware that targeted Siemens S7 controllers driving uranium-enrichment centrifuges at Natanz, Iran. It crossed an air gap on removable media, changed centrifuge speeds, and replayed normal-looking values to the operators while it did so.

**Lesson:** an air gap is not a control by itself, because people carry things across it. And what the HMI shows is not proof of what the process is doing.

## Ukraine power grid (December 2015)

Attackers got into three electricity distribution companies through spear-phishing, harvested credentials, and used the companies' own remote access and SCADA software to open breakers. About 225,000 customers lost power. The attackers also wiped workstations, corrupted firmware on serial-to-Ethernet converters, and flooded the call centers.

**Lesson:** no exotic exploit was needed. Legitimate remote access with stolen credentials was enough. MFA and separation between IT credentials and OT access matter more than any single patch.

## Industroyer / CrashOverride (December 2016)

A second attack in Ukraine, on a transmission substation near Kyiv. This time the malware spoke grid protocols (including IEC 60870-5-104 and IEC 61850) directly, with no human operating an HMI.

**Lesson:** the protocols have no authentication, so software that can reach the devices can command them. Reachability is the control.

## TRITON / TRISIS (2017)

Malware aimed at the Schneider Electric Triconex safety instrumented system at a petrochemical plant in the Middle East. A mistake by the attackers tripped the safety system and shut the plant down, which led to discovery. The controllers' key switches had been left in program mode, which allowed remote changes.

**Lesson:** safety systems are targets. Keep them on their own network, keep the key switch out of program mode, and treat an unexplained safety trip as a possible security event.

## Oldsmar water treatment (February 2021)

An operator at a Florida water plant saw the sodium hydroxide setpoint change from about 100 to 11,100 parts per million through remote-access software, and reversed it at once. Later reporting raised doubt about whether an outside intruder was responsible.

**Lesson:** whatever the cause, the conditions were real: shared remote-desktop software on a control workstation and an alert operator as the main safeguard. Setpoint limits enforced in the controller are a better one.

## Colonial Pipeline (May 2021)

Ransomware hit the company's IT network, reportedly through a VPN account that had no MFA. The pipeline's control systems were not shown to be affected, but the company shut the pipeline down for several days as a precaution, and paid a ransom of about $4.4 million.

**Lesson:** an IT incident can stop operations even when OT is untouched, if the business can't run or can't be sure OT is clean. Know in advance whether you could keep operating with IT down, and whether you could prove OT is isolated.

## What the cases have in common

- Entry through IT or remote access, not through a PLC.
- Long dwell time before the physical effect.
- Use of the victim's own tools and protocols.
- Detection by people noticing something physical, rather than by security tooling.

That list maps almost one-to-one onto the basics: segmentation, controlled remote access with MFA, monitoring inside OT, and tested recovery.

## Sources

- CISA alert on the 2015 Ukraine attack: <https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01>
- CISA alert on CrashOverride: <https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware>
- MITRE ATT&CK, Triton Safety Instrumented System Attack: <https://attack.mitre.org/campaigns/C0030/>
- CISA advisory on Schneider Electric Triconex: <https://www.cisa.gov/news-events/ics-advisories/icsa-18-107-02>
- CISA advisory on the Oldsmar compromise: <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA advisory on DarkSide ransomware (Colonial Pipeline): <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a>
- MITRE ATT&CK for ICS, software and campaign entries: <https://attack.mitre.org/matrices/ics/>

Previous: [6. Standards and frameworks](06-standards.md) · See also: [Resources](../resources.md)

# 5. Remote access

Remote access is how many OT incidents start: a VPN account without MFA, a remote-desktop tool left running on an HMI, a vendor modem nobody remembered. It's also something the plant needs, because the vendor who can fix the machine is often in another country. The goal is to control it, not to ban it.

## Find what exists

Expect more paths than the firewall shows:

- Site-to-site and client VPNs from corporate IT
- Vendor VPN appliances and cellular gateways inside machine cabinets
- Remote-desktop tools (TeamViewer, AnyDesk, VNC) installed on HMIs or engineering PCs
- Cloud-managed "remote service" boxes that dial out from the machine network
- Dual-homed laptops that integrators plug in and leave

Check firewall logs for outbound connections from OT, ask each vendor how they connect, and open the cabinets.

## A pattern that works

```
Remote user ──MFA──> VPN / access gateway ──> Jump host in the DMZ ──> one target in OT
```

1. **MFA at the edge.** Every remote user, including vendors.
2. **Land in the DMZ.** The VPN reaches a jump host, never OT directly.
3. **Second hop.** From the jump host, a separate session (RDP, vendor software) to the specific machine. Firewall rules allow the jump host to reach only named targets on named ports.
4. **Named accounts.** One per person. No shared "vendor" login.
5. **Off by default.** Vendor accounts are disabled until someone at the plant enables them for a job, and they expire.
6. **Someone on site knows.** Operations is told before a remote session touches a running process. Remote changes to a live machine can hurt the person standing next to it.
7. **Logged.** Who connected, when, to what. Record sessions where you can.

## Rules for vendors

Put these in the purchase order or support contract, before the machine arrives:

- Access goes through the plant's gateway, not a vendor-supplied modem or always-on tunnel.
- Named individuals, MFA, access on request for a stated time window.
- No remote program changes without a person on site and an approved change.
- The vendor reports security incidents on their side that affect the access path.

Machine builders will push back because their own tool is easier for them. A compromise that often works: their tool is allowed, but it runs only on the jump host and only when enabled.

## Common mistakes

- A VPN that drops the user onto the whole OT subnet.
- Remote-desktop software on an HMI with a shared password and direct internet access.
- One vendor account used by an entire support team.
- Access that was opened for commissioning and never closed.
- Accounts of people who left the vendor years ago.
- No way to cut remote access quickly. Decide in advance who can disable it and how.

## Sources

- CISA and NSA guidance on securing remote access software: <https://www.cisa.gov/resources-tools/resources/guide-securing-remote-access-software>
- NIST SP 800-82 Rev. 3: <https://csrc.nist.gov/pubs/sp/800/82/r3/final>

Previous: [4. Your first 90 days](04-first-90-days.md)

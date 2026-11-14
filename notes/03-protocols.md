# 3. Industrial protocols: what an IT person needs to know

Most industrial protocols were designed for isolated serial links, where anyone on the wire was trusted. They were later wrapped in TCP/IP with the same assumption. In many of them, **reaching the device is the same as being authorized to control it.**

## Quick reference

| Protocol | Default port | Common in | Built-in security |
|---|---|---|---|
| Modbus TCP | 502/tcp | Almost everything | None. No authentication, no encryption |
| EtherNet/IP (CIP) | 44818/tcp, 2222/udp | Rockwell / Allen-Bradley | None by default. CIP Security adds TLS on newer devices |
| S7comm | 102/tcp | Siemens S7 | Weak on older PLCs. Newer firmware adds integrity protection and TLS |
| PROFINET | Layer 2 | Siemens and others | None in most deployed versions |
| DNP3 | 20000/tcp | Electric and water utilities | Optional Secure Authentication, rarely enabled |
| BACnet/IP | 47808/udp | Building automation | None by default. BACnet/SC adds TLS |
| OPC Classic (DA) | 135/tcp plus dynamic ports | Older Windows integrations | Relies on DCOM. Hard to firewall |
| OPC UA | 4840/tcp | Modern integration layer | Certificates, signing, encryption and user authentication |

Ports are the registered defaults. Vendors and integrators change them, so confirm with a capture.

## What "no security" means

Take Modbus. A request is a function code and an address: read these registers, write this coil. There's no login and no session. Anyone who can open a TCP connection to port 502 can read process values and write outputs. The same applies to starting, stopping or reprogramming many older PLCs over their native protocols.

So the protection has to come from outside the protocol:

- **Network position.** Only the HMIs and engineering stations that need a controller can reach it.
- **Protocol-aware firewalls.** Some industrial firewalls can allow Modbus reads while blocking writes, or block program downloads.
- **Physical controls on the PLC.** A key switch in RUN rather than PROGRAM, and memory protection where the controller supports it.
- **Monitoring.** A write or program download from an unusual source is a high-quality alert, because normal OT traffic is repetitive.

## OPC UA is different, if you configure it

OPC UA was designed with security in mind, but it ships with insecure options for compatibility:

- **Security mode** can be `None`, `Sign` or `SignAndEncrypt`. Disable `None` on the server.
- **Certificates.** Servers and clients each have one. Don't leave "automatically trust all client certificates" on after commissioning.
- **User authentication.** Anonymous access is often enabled by default. Turn it off, and separate read-only users from users who can write.
- **Old security policies** (`Basic128Rsa15`, `Basic256`) are deprecated. Use `Basic256Sha256` or newer.

## Reading traffic safely

- Wireshark has dissectors for all of the protocols above. Capture from a SPAN port or tap rather than from a production machine.
- Passive first. Don't send traffic to a controller until you know how it reacts.
- Learn the write and program functions for the protocols in your plant, then alert on them.
- Practice in a lab. Simulators exist for Modbus, OPC UA and others, and they cost nothing to crash.

## Sources

- OPC Foundation, security resources: <https://opcfoundation.org/security/>
- MITRE ATT&CK for ICS (techniques built on these protocol weaknesses): <https://attack.mitre.org/matrices/ics/>

Previous: [2. The Purdue model and segmentation](02-purdue-and-segmentation.md)

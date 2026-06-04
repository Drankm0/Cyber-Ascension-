# System Discovery Lab

## Objective

Learn how to identify open ports, investigate running services, and verify process ownership on a macOS system.

## Commands Used

nmap localhost

lsof -i :5000

lsof -i :7000

ps -p 440 -o pid,ppid,user,command

nmap -sV localhost

## Findings

### Port 5000

- Process: ControlCenter
- PID: 440
- Service Detection: AirTunes/870.14.1

### Port 7000

- Process: ControlCenter
- PID: 440
- Service Detection: AirTunes/870.14.1

## Conclusion

Nmap service names do not always represent the actual service running on a port. Verification should be performed using lsof, ps, and service detection techniques.

## Skills Practiced

- Port Enumeration
- Service Discovery
- Process Identification
- Network Troubleshooting
- System Administration


# System Discovery Lab

Testing Nmap, lsof, ps, and service discovery on macOS.

## Findings

- Port 5000 -> ControlCenter
- Port 7000 -> ControlCenter
- AirTunes detected

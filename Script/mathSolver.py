from pwn import *

r = remote('192.168.3.100',6699)

for i in range(1,11):
    r.recvuntil('No: (%d) ' % i)
    calc = r.recvuntil('=>', drop=True)
    print ('%d %s' % (i , str(eval(calc))))
    r.send(str(eval(calc)) + '\n')

print (r.recvall())
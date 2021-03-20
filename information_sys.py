import os

fields = os.uname()

print('sysversion___________', fields.sysname)
print('version______________', fields.version)
print('nodename_____________', fields.nodename)
print('machine_arch_________', fields.machine)
print('release______________', fields.release)



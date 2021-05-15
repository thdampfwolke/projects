#!/usr/bin/python3

import socket

# ------------------------------------------------
print('01', '-' * 50)
print(socket.gethostname())

# ------------------------------------------------
HOSTS = ['oreilly.com', 'mail.google.com', 'www.python.org', 'nosuchname']

# ------------------------------------------------
print('02', '-' * 50)
for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))

# ------------------------------------------------
print('03', '-' * 50)
for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print(' Hostname:', name)
        print(' Aliases :', aliases)
        print(' Addresses:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
        print()

# ------------------------------------------------
print('04', '-' * 50)
for host in HOSTS:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))

# ------------------------------------------------
print('05', '-' * 50)
hostname, aliases, addresses = socket.gethostbyaddr('192.168.2.24')
print('Hostname :', hostname)
print('Aliases :', aliases)
print('Addresses:', addresses)

# ------------------------------------------------
print('06', '-' * 50)



"""

============== RESTART: C:\projects\py__dns\dns_02.py =============
01 --------------------------------------------------
dargo-nb-lenovo
02 --------------------------------------------------
oreilly.com : 199.27.145.65
mail.google.com : 142.250.184.197
www.python.org : 151.101.12.223
nosuchname : [Errno 11001] getaddrinfo failed
03 --------------------------------------------------
oreilly.com
 Hostname: oreilly.com
 Aliases : []
 Addresses: ['199.27.145.65', '199.27.145.64']
mail.google.com
 Hostname: googlemail.l.google.com
 Aliases : ['mail.google.com']
 Addresses: ['142.250.184.197']
www.python.org
 Hostname: dualstack.python.map.fastly.net
 Aliases : ['www.python.org']
 Addresses: ['151.101.12.223']
nosuchname
ERROR: [Errno 11001] getaddrinfo failed

04 --------------------------------------------------
oreilly.com : oreilly.com
mail.google.com : fra24s11-in-f5.1e100.net
www.python.org : www.python.org
nosuchname : nosuchname
05 --------------------------------------------------
Hostname : dargo-nb-lenovo.fritz.box
Aliases : []
Addresses: ['192.168.2.24']
06 --------------------------------------------------

"""

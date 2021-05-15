#!/usr/bin/python3

import dns.resolver

host = "oreilly.com"
host2 = "mail.google.com"

dns_res_a = dns.resolver.resolve(host, "A")
for dns_a in dns_res_a:
    print('ip: ', dns_a)

dns_res_mx = dns.resolver.resolve(host, "MX")
for dns_mx in dns_res_mx:
    print('mx: ', dns_mx)

dns_res_cn = dns.resolver.resolve(host2, "CNAME")
for dns_cn in dns_res_cn:
    print('cn: ', dns_cn)

# mail = dns.resolver.query("oreilly.com","MX")


#for i,p in ip,mail:
#    print(i, p)


"""
import dns.resolver
ip = dns.resolver.query("oreilly.com","A")
mail = dns.resolver.query("oreilly.com","MX")

for i,p in ip,mail:
    print(i, p)
"""


"""
#import dnspython as dns
import dns.resolver

result = dns.resolver.query('tutorialspoint.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())

#!/usr/bin/python3

import dns.resolver

answers = dns.resolver.resolve('dnspython.org', 'A')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)
"""

#!/usr/bin/python3

# import os
# print(dir(os))

# -----------------------------------------------
def del_char(f_a):
    f_list = ["{", "}", "[", "]", "'"]
    for i in f_list:
        f_a = f_a.replace(i, "")
    return f_a

# -----------------------------------------------
def dns_A(f_reply, f_i):        # 'A': ['1.2.3.4']
    f_reply_A = f_reply[f_i].split(":")
    f_dns_type = del_char(f_reply_A[0]).strip()  # -> A
    f_hostname_CN = ""
    f_hostname_IP = del_char(f_reply_A[1]).strip()  # -> 1.2.3.4
    if f_dns_type != "A":
        f_dns_type = "error"
        print("error: A-Record")
    return (f_dns_type, f_hostname_CN, f_hostname_IP)

# -----------------------------------------------
def dns_C(f_reply, f_i):        # 'CNAME': ['host--1-2-3-4.test.de']
    f_reply_C = f_reply[f_i].split(":")
    f_dns_type = del_char(f_reply_C[0]).strip()  # -> CNAME
    f_hostname_C = del_char(f_reply_C[1]).strip()
    if f_dns_type != "CNAME":
        f_dns_type = "error"
        print("error: CNAME")
    return (f_dns_type, f_hostname_C)

# -----------------------------------------------
def dns_I(f_reply, f_i):        # ('host--1-2-3-4.test.de', ['host--1-2-3-4'], ['1.2.3.4'])
    f_reply_A = f_reply[f_i].split(":")
    f_dns_type = del_char(f_reply_A[0]).strip()  # -> A
    f_hostname_CN = ""
    f_hostname_IP = del_char(f_reply_A[1]).strip()  # -> 1.2.3.4
    if f_dns_type != "A":
        f_dns_type = "error"
        print("error: A-Record")
    return (f_dns_type, f_hostname_CN, f_hostname_IP)

# ----------------------------------------------------------------------------
a1 = "9.9.9.9;hOSt--1-2-3-4.test.de;{'A': ['1.2.3.4']}"
#a1 = "9.9.9.9;host--2-3-4-5.test.de;{'CNAME': ['host--1-2-3-4.test.de'], 'A': ['1.2.3.4']}"
#a1 = "9.9.9.9;host--3-4-5-6.test.de;{'A': ['3.4.5.6']}"
# b1 = ('host--3-4-5-6.test.de', [], ['3.4.5.6'])
b1 = ('host--1-2-3-4.test.de', ['host--1-2-3-4'], ['1.2.3.4'])
# ----------------------------------------------------------------------------
deb = "a"
# ----------------------------------------------------------------------------

if deb == "a":
    a = a1.split(";")
    dns_server = a[0]           # -> 9.9.9.9
    hostname_request = a[1]     # -> host--2-3-4-5.test.de
    hostname_reply = a[2]       # ->
    reply = hostname_reply.split(",", 1)

    if len(reply) == 1:     # A-Record      # {'A': ['1.2.3.4']}"
        dns_type, hostname_CN, hostname_IP = dns_A(reply, 0)
    else:  # CNAME          # {'CNAME': ['host--1-2-3-4.test.de'], 'A': ['1.2.3.4']}
        dns_type_tmp, hostname_CN_tmp, hostname_IP = dns_A(reply, 1)
        dns_type, hostname_CN = dns_C(reply, 0)

elif deb == "b":            # ('host--1-2-3-4.test.de', ['host--1-2-3-4'], ['1.2.3.4'])
    a = b1
    dns_type = "A"
    # dns_server = ""
    hostname_IP = del_char(str(a[2]))           # -> request
    hostname_request = del_char(str(a[0]))      # -> reply
    hostname_CN = ""
    print(f"b")
else:
    print(f"else: {deb}")

print(f"dns_type: {dns_type} \t hostname_request: {hostname_request} \t hostname_CN: {hostname_CN} \t hostname_IP: {hostname_IP}")
print(f"{dns_type.upper()};{hostname_request.lower()};{hostname_CN.lower()};{hostname_IP.lower()}")

#with open("99_31__data.txt", "r") as f_in:
#  new_data = sorted(list(set(f_in)))
#  # return new_data
#print(f"anzahl: {len(new_data)} \t {new_data}")
#  #print(f"anzahl: {len(new_data)} \t {sorted(new_data)}")

"""

https://stackoverflow.com/questions/24891623/sort-and-uniq-in-python
call('sort {0} | uniq'.format(FileOut), shell=True)

https://www.codegrepper.com/code-examples/python/remove+duplicate+sentences+directly+write+text+file+python
lines_seen = set() # holds lines already seen
with open("file.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
    f.truncate()

or
with open("file.txt", "r") as txt_file:
  new_data = list(set(txt_file))
  return new_data


# -----------------------------------------------
# da_ou_ho.txt
# dns-server; hostname; A:      IP
# dns-server; hostname; CNAME:  hostname, IP

9.9.9.9;host--1-2-3-4.test.de;{'A': ['1.2.3.4']}
9.9.9.9;host--2.3.4.5.test.de;{'CNAME': ['host--1-2-3-4.test.de'], 'A': ['1.2.3.4']}
9.9.9.9;host--3-4-5-6.test.de;{'A': ['3.4.5.6']}

# -----------------------------------------------
# da_ou_ip.txt
# hostname, hostnames, IPs

('host--1-2-3-4.test.de', ['host--1-2-3-4'], ['1.2.3.4'])
('host--3-4-5-6.test.de', [], ['3.4.5.6'])
"""


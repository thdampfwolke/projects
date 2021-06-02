#!/usr/bin/python3

with open("99_31__data.txt", "r") as f_in:
  new_data = sorted(list(set(f_in)))
  # return new_data

print(f"anzahl: {len(new_data)} \t {new_data}")

#lines_seen = set() # holds lines already seen
#
#with open("99_31__data.txt", "r+") as f:
#    d = f.readlines()
#    f.seek(0)
#    for i in d:
#        if i not in lines_seen:
#            f.write(i)
#            lines_seen.add(i)
#    f.truncate()
#print(lines_seen)
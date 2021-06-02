#!/usr/bin/python3

with open("test_sort-uniq_data.txt", "r") as f_in:
    new_data = sorted(list(set(f_in)))
    # return new_data
print(f"anzahl: {len(new_data)} \t {new_data}")
#print(f"anzahl: {len(new_data)} \t {sorted(new_data)}")

data_my = []
n = 0
for i in new_data:
    n += 1
    print(f"{n} \t {i.strip()}")
    data_my.append(i.strip())

print(data_my)
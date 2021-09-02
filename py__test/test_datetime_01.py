#!/usr/bin/python3

from datetime import timedelta
from datetime import datetime
a = datetime(2012, 9, 23)

print(a + timedelta(days=10))

b = datetime(2012, 12, 21)
d = b - a
print(d.days)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))


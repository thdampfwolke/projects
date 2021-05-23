#!/usr/bin/python3

import time

try:
    with (
        open("y_file_in.txt",  "r") as f_in,
        open("y_file_out.txt", "w") as f_out
    ):
        print(time.strftime("Time:  %d.%m.%Y  -  %H:%M:%S"))
        print("try: with: ok")
        f_out.write(f_in.read())
except FileNotFoundError as e:
    print("error       : FileNotFoundError")
    print("error       : ", e)
    print("error - type: ", type(e))
except Exception as e:
    print("error       : all-other")
    print("error       : ", e)
    print("error - type: ", type(e))
#else:
#    print("try: else: ok")
finally:
    print("try: finally: end")
    print(time.strftime("Time:  %d.%m.%Y  -  %H:%M:%S"))

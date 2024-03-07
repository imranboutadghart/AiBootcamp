import sys

arg = sys.argv
if len(arg) < 2:
    exit()
if len(arg) > 2 or (len(arg) == 2 and not arg[1].isdigit()):
    print("AssertionError")
    exit()

if (int(arg[1]) % 2 == 0):
    print("I'm Even")
else:
    print("I'm odd")

#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print(total)

#!/usr/bin/python3
import hidden_4

all_names = dir(hidden_4)

for name in sorted(all_names):
    if not name.startswith("__"):
        print(name)

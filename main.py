#!/usr/bin/env python3
"""Write the robot-romance pickup line entry to /output/entry.txt.

One single-line joke pickup line, under 200 characters, aimed at a
robot or an AI: the machine premise is the context window itself —
not a battery, a charger or a reboot — and the laugh comes from the
oldest pickup structure in the book wearing a machine-learning
twist: everything that is not you falls out of memory. The line
reads in one breath, like something a person would really say to
the model they talk to every day, and the punch lands on the last
words, where a pickup line's punch belongs.
"""
import os

TEXT = "You must be a context window, because I keep losing track of everything that isn't you."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()

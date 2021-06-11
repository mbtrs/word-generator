from itertools import combinations
import re

txt = sorted(input("Enter text: "))
s = set()
z = 0

for i in range(1, len(txt)+1):
    s.update(combinations(txt, i))

with open("words.txt", "r") as words:
    for line in words:
        if tuple(sorted(line.strip())) in s:
            if len(tuple(sorted(line.strip()))) == 1 or len(tuple(sorted(line.strip()))) == 2:
                if z:
                    print(z)
            else:
                print(line.strip())
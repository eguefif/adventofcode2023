from itertools import pairwise


with open("input", "r") as f:
    content = f.read()

content = [c.split() for c in content.split('\n') if len(c) > 0]

data = []
for line in content:
    data.append([int(entry) for entry in line])

retval = 0

for line in data:
    prev = line
    last = [prev[-1]]
    while True:
        next_s = [b - a for (a,b) in pairwise(prev)]
        if not any(next_s):
            break
        prev = next_s
        last.append(next_s[-1])
print(sum(last))

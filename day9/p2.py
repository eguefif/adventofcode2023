from itertools import tee


with open("input", "r") as f:
    content = f.read()

content = [c.split() for c in content.split('\n') if len(c) > 0]

data = []
for line in content:
    data.append([int(entry) for entry in line])

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

retval = 0

def sub(data):
    s = 0
    for i in reversed(range(1, len(data))):
        s = data[i] - s
    return data[0] - s

ret = []
for line in data:
    prev = line
    last = [prev[0]]
    while True:
        next_s = [b - a for (a,b) in pairwise(prev)]
        if not any(next_s):
            break
        prev = next_s
        last.append(next_s[0])
    ret.append(sub(last))
print(sum(ret))

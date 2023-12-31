from itertools import tee


with open("input_ex", "r") as f:
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

ret = []
for line in data:
    prev = line
    last = [prev[-1]]
    while True:
        next_s = [b - a for (a,b) in pairwise(prev)]
        if not any(next_s):
            break
        prev = next_s
        last.append(next_s[-1])
    ret.append(sum(last))
print(sum(ret))

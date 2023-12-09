from multiprocessing import Process
import numpy as np
with open("input", "r") as f:
    content = f.read()

directions, content = content.split("\n\n")
content = content.split("\n")[:-1]
lab = {}
for line in content:
    sp = line.split(" = ")
    left, right = sp[1].split(",")
    left = left.strip("(")
    right = right.strip(" )")
    lab[sp[0]] = [
            left,
            right]
    #entry = {"node": sp[0],

lr = {"L": 0, "R": 1}

starts = [s for s in lab.keys() if s[2] == 'A']

def get_nbr(lab, directions, start):
    i = 0
    current = start
    while current[2] != "Z":
        for d in directions:
            direction = lr[d]
            current = lab[current][direction]
            i+=1
            if current[2] == "Z":
                return i
    return i

def lcm(l):
    return math.prod(l)/math.gcd(*l)
    c = max(l) + 1
    p = math.prod(l)
    while c != p:
        c += 1
    return c

l = []
for start in starts:
    l.append(get_nbr(lab, directions, start))

data = np.array(l)

print(np.lcm.reduce(data))

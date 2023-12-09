from multiprocessing import Process
with open("input", "r") as f:
    content = f.read()

directions, content = content.split("\n\n")
content = content.split("\n")
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
print(starts)
def is_everybody_ends(currents):
    cond = [c[2] == "Z" for c in currents]
    return (all(cond))

def print_current(currents, direction):
    print("Direciton :", direction, "CUrrents:" , currents)

def get_nbr(lab, directions, starts):
    i = 0
    currents = starts
    while not is_everybody_ends(currents):
        for d in directions:
            direction = lr[d]
            new_c = []
            for current in currents:
                new_c.append(lab[current][direction])
            currents = new_c
            i+=1
    return i

print(get_nbr(lab, directions, starts))

from multiprocessing import Process, Value, Array

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
result = {k:v for (k, v) in zip(starts, [0] * 9)}
def get_nbr(lab, directions, starts):
    i = 0
    current = starts
    while current != "ZZZ":
        for d in directions:
            direction = lr[d]
            current = lab[current][direction]
            i+=1
            if current == "ZZZ":
                return i
    

"""
i = 0
processes = [
        Process(target=get_nbr, args=(lab, directions, s)) for s in starts]

for p in processes:
    p.start()

while processes:
    processes.pop().join()
    """

print(result)

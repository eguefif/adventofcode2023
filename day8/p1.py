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

def get_nbr(lab, directions):
    i = 0
    current = "AAA"
    while current != "ZZZ":
        for d in directions:
            direction = lr[d]
            current = lab[current][direction]
            i+=1
            if current == "ZZZ":
                return i

print(get_nbr(lab, directions))

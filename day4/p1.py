with open("input", "r") as f:
    content = f.read()
content = content.split("\n")[:-1]

cards = []


for line in content:
    win = []
    mine = []
    line = line.split(":")[1].strip()
    line = line.split("|")
    win = line[0].split()
    mine = line[1].split()
    cards.append((win, mine))

retval = 0
for c in cards:
    m = 0
    for card in c[1]:
        if card in c[0]:
            if m == 0:
                m = 1
            else:
                m *= 2
    retval += m
print(retval)

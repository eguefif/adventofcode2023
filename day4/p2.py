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

retval = [1 for _ in range(len(content))]

for i, c in enumerate(cards):
    m = 0
    for card in c[1]:
        if card in c[0]:
            m += 1
    print(f"line {i} has {m} matches.", end="")
    for win in range(m):
        if win + i + 1 < len(retval):
            retval[win + i + 1] += retval[i]
    print(f"Retval: {retval[:15]}")


print(sum(retval))

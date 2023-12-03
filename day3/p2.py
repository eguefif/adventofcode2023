with open("input", "r") as f:
    content = f.read();
content = content.split("\n")[:-1]


symbol = []
numbers = []
def get_nbr_(line, x):
    nbr = 0
    for c in line[x:]:
        if not c.isdigit():
            break
        nbr *= 10
        nbr += int(c)
    return (nbr)

for y, line in enumerate(content):
    x = 0
    while x < len(line):
        if line[x].isdigit():
            nbr = get_nbr_(line, x)
            numbers.append({"number": nbr, "x": x, "y": y})
            while x < len(line) and line[x].isdigit():
                x += 1
        else :
            x += 1


for y, line in enumerate(content):
    x = 0
    for x, c in enumerate(line):
        if line[x] == '*':
            symbol.append((x, y))

def get(content, x, y):
    for i in range(-2, 3):
        for n in numbers:
            if n["x"] == x + i and n["y"] == y:
                return n["number"]


def is_nbr_top(star, content):
    if content[star[0]][star[1] + 1].isdigit():
        return True


def get_nbr(star, content):
    n = []
    if content[star[0] - 1][star[1]].isdigit():
        n.append(get(content, star[0] - 1, star[1]))
    if content[star[0] + 1][star[1]].isdigit():
        n.append(get(content, star[0] + 1, star[1]))
    if content[star[0]][star[1] - 1].isdigit():
        n.append(get(content, star[0], star[1] - 1))
    if content[star[0]][star[1] + 1].isdigit():
        n.append(get(content, star[0], star[1] + 1))
    if content[star[0] + 1][star[1 + 1]].isdigit():
        n.append(get(content, star[0] + 1, star[1] + 1))
    if content[star[0] + 1][star[1] - 1].isdigit():
        n.append(get(content, star[0] + 1, star[1] - 1))
    if content[star[0] - 1][star[1] + 1].isdigit():
        n.append(get(content, star[0] - 1, star[1] + 1))
    if content[star[0] - 1][star[1] - 1].isdigit():
        n.append(get(content, star[0] - 1, star[1] - 1))
    if (len(n) == 2):
        return n[0], n[1]
    return 0, 0


retval = 0

for star in symbol[:3]:
    n1, n2 = get_nbr(star, content)
    if n1 != 0:
        retval += (n1 * n2)

print(retval)

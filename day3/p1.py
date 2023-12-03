with open("input", "r") as f:
    content = f.read();
content = content.split("\n")[:-1]


symbol = []
numbers = []

def get_nbr(line, x):
    nbr = 0
    for c in line[x:]:
        if not c.isdigit():
            break
        nbr *= 10
        nbr += int(c)
    return (nbr)

def get_nbr_size(nbr):
    i = 0
    while int(nbr) > 0:
        nbr = int(nbr / 10)
        i += 1
    return i

for y, line in enumerate(content):
    x = 0
    while x < len(line):
        if line[x] != '.' and not line[x].isdigit():
            symbol.append((x, y))
            x += 1
        elif line[x].isdigit():
            nbr = get_nbr(line, x)
            numbers.append({"number": nbr, "x": x, "y": y, "size": get_nbr_size(nbr), })
            while x < len(line) and line[x].isdigit():
                x += 1
        else :
            x += 1

def is_valid(nbr, symbol):
    for i in range(0, nbr["size"]):
        a = (nbr["x"] + i - 1, nbr["y"])
        b = (nbr["x"] + i + 1, nbr["y"])
        c = (nbr["x"] + i, nbr["y"] + 1)
        d = (nbr["x"] + i, nbr["y"] - 1)
        e = (nbr["x"] + i - 1, nbr["y"] - 1)
        f = (nbr["x"] + i - 1, nbr["y"] + 1)
        g = (nbr["x"] + i + 1, nbr["y"] + 1)
        h = (nbr["x"] + i + 1, nbr["y"] - 1)
        if (a in symbol or b in symbol or c in symbol or d in symbol or
                e in symbol or f in symbol or g in symbol or h in symbol):
            return True
    return False

retval = 0

for nbr in numbers:
    if is_valid(nbr, symbol):
        retval += nbr["number"]

print(retval)

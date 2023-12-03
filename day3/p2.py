with open("input", "r") as f:
    content = f.read();
content = content.split("\n")[:-1]

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

stars = []
numbers = []

for y, line in enumerate(content):
    x = 0
    while x < len(line):
        if line[x] == '*':
            stars.append((x, y))
            x += 1
        elif line[x].isdigit():
            nbr = get_nbr(line, x)
            numbers.append({"number": nbr, "x": x, "y": y, "size": get_nbr_size(nbr), })
            while x < len(line) and line[x].isdigit():
                x += 1
        else :
            x += 1

def get_nbr_around(star, numbers):
    retval = []
    for n in numbers:
        for i in range(n["size"]):
            if abs(n["x"] + i - star[0]) in [0, 1] and abs(n["y"] - star[1]) in [0, 1]:
                retval.append(n["number"])
                break
    return retval

n = 0;

for star in stars:
   value = get_nbr_around(star, numbers) 
   if len(value) == 2:
       n += (value[0] * value[1])

print(n)

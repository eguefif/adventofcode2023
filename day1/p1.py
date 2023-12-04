with open("input", "r") as f:
    content = f.read()
content = content.split("\n")[:-1]

def get_number(line):
    first = 0
    last = 0
    for c in line:
        if c.isnumeric():
            if (first == 0):
                first = c
            else:
                last = c
    if last == 0:
            return int(first) * 10 + int(first)
    return int(first) * 10 + int(last)

tab = []
for line in content:
    tab.append(get_number(line))
print(sum(tab))

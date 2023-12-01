with open("input", "r") as f:
    content = f.read()
content = content.split("\n")
content.pop()
tab = []

def get_number(line):
    first = 0
    last = 0
    for idx, c in enum(line):
        if c.isnumeric():
            if (first == 0):
                first = c
            else:
                last = c
    if last == 0:
            return int(first) * 10 + int(first)
    return int(first) * 10 + int(last)

for line in content:
    tab.append(get_number(line))
print(sum(tab))

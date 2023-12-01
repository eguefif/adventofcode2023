with open("input", "r") as f:
    content = f.read()
content = content.split("\n")
content.pop()
tab = []

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_number(line):
    first = 0
    last = 0
    for idx, c in enumerate(line):
        if c.isnumeric():
            if (first == 0):
                first = c
            else:
                last = c
            continue
        for nbr, digit in enumerate(numbers):
            if line[idx:].find(digit) == 0:
                if first == 0:
                    first = int(nbr) + 1
                else:
                    last = int(nbr) + 1
    if last == 0:
            return int(first) * 10 + int(first)
    return int(first) * 10 + int(last)

for line in content:
    tab.append(get_number(line))
    #print(line, ":", tab[-1])
print(sum(tab))

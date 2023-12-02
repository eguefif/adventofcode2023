with open("input", "r") as f:
    content = f.read()

content = content.split("\n")[:-1]

def get_values(line):
    idx = line.find(":")
    sets = line[idx + 1:].split(";")
    s = {"red": [], "green": [], "blue": []}
    for sset in sets:
        colors = sset.split(",")
        for color in colors:
            color = color.strip()
            if color.find("red") != -1:
                s["red"].append(int(color.split(" ")[0]))
            elif color.find("green") != -1:
                s["green"].append(int(color.split(" ")[0]))
            elif color.find("blue") != -1:
                s["blue"].append(int(color.split(" ")[0]))
    return s

def get_power(values):
    return max(values["red"]) * max(values["blue"]) * max(values["green"])

nbr = 0;
for line in content:
    values = get_values(line)
    nbr += get_power(values)

print(nbr)

with open("input", "r") as f:
    content = f.read()
content = content.split("\n")[:-1]


def get_values(line):
    idx = line.find(":")
    sets = line[idx + 1:].split(";")
    values = []
    for sset in sets:
        s = {"red": 0, "green": 0, "blue": 0}
        colors = sset.split(",")
        for color in colors:
            color = color.strip()
            if color.find("red") != -1:
                s["red"] = int(color.split(" ")[0])
            elif color.find("green") != -1:
                s["green"] = int(color.split(" ")[0])
            elif color.find("blue") != -1:
                s["blue"] = int(color.split(" ")[0])
        values.append(s)

    return values

def is_valid_game(values):
    for value in values:
        if value["red"] > 12 or value["green"] > 13 or value["blue"] > 14:
            return False
    return True

nbr = 0;
for i, line in enumerate(content):
    values = get_values(line)
    if is_valid_game(values):
        nbr += (i + 1)

print(nbr)

from collections import Counter

with open("input", "r") as f:
    content = f.read()
content = content.split("\n")[:-1]
data = []
content = [line.split() for line in content]

hands = []

card = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8":7, "9": 8, "T": 9,
        "J": 0, "Q": 11, "K": 12, "A": 13}

def get_type(hand):
    c = dict(Counter(hand))
    if 5 in c.values():
        return 7
    if 4 in c.values():
        return 6
    if 2 in c.values() and 3 in c.values():
        return 5
    if 3 in c.values():
        return 4
    pairs = 0
    for v in c.values():
        if v == 2:
            pairs += 1

    if pairs == 2:
        return 3
    if pairs == 1:
        return 2
    return 1

def get_pair_nbr(hand):
    pairs = 0
    c = dict(Counter(hand))
    for v in c.values():
        if v == 2:
            pairs += 1
    if pairs == 2:
        return 2
    if pairs == 1:
        return 1
    return 0


def get_type_j(hand):
    c = Counter(hand)
    if "J" not in c.keys():
        return  -1
    j_nbr = c["J"]
    c.pop("J")
    most = c.most_common(5)
    if (len(most) == 0):
        return 0
    if most[0][1] + j_nbr >= 5:
        return 7
    if most[0][1] + j_nbr == 4:
        return 6
    if most[0][1] == 2 and j_nbr >= 1:
        return 4
    if most[0][1] == 1 and j_nbr >= 1:
        return 2
    return 1


def replace(s):
    retval = []
    for e in s:
        retval.append(card[e])
    return retval

def get_highest(hand):
    s = replace(hand)
    return s

for entry in content:
    hand = {"type": max(get_type(entry[0]), get_type_j(entry[0])),
            "high": get_highest(entry[0]),
            "bid": int(entry[1]),
            "hand": entry[0]
            }
    hands.append(hand)

def custom_sort(item1, item2):
    if item1["type"] < item2["type"]:
        return -1
    elif item1["type"] > item2["type"]:
        return 1
    for h1, h2 in zip(item1["high"], item2["high"]):
        if h1 < h2:
            return -1
        elif h1 > h2:
            return 1
    return 0

for i in range(len(hands)):
    for j in range(i + 1, len(hands)):
        if custom_sort(hands[i], hands[j]) > 0:
                tmp = hands[i]
                hands[i] = hands[j]
                hands[j]  = tmp

solution = 0
for i, h in enumerate(hands):
    solution += (i+1) * h["bid"]
    print(i+1, h, (i+1) * h["bid"])
print(solution)

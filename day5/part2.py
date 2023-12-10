from multiprocessing import Process


with open("input", "r") as f:
    content = f.read()

content = content.split("\n\n")
seeds = [int(x) for x in content[0].split(":")[1].split()]
content = content[1:]

pipes = []
l = max(seeds * 1000)
for t in content[:-1]:
    pipe = t.split("\n")[1:]
    tmp = []
    for p in pipe:
        tmp.append([int(n) for n in p.split()])
    pipes.append(tmp)

seeds = [79, 14, 55, 13]
pipes = [[[50, 98, 2], [52, 50, 48]],
        [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
        [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
        [[88, 18, 7], [18, 25, 70]],
        [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        [[0, 69, 1],[ 1, 0, 69]],
        [[ 60, 56, 37], [56, 93, 4]]]

pipeline = []
for p in pipes:
    pipe = []
    new_pipe = []
    for line in p:
        info = {"translation": line[1] - line[0],
                "start": line[1],
                "end": line[1] + line[2],
                "offset": line[2],
                }
        new_pipe.append(info)
    pipeline.append(new_pipe)

def apply_pipe(r, stretch):
    former_low = r[0]
    former_high = r[1]
    if stretch["start"] <= r[0]:
        low = r[0] - stretch["translation"]
        former_low = low
    else:
        low = stretch["start"] - stretch["translation"] 
    if stretch["end"] <= r[1]:
        high = stretch["end"] - stretch["translation"]
    else:
        high = r[1] - stretch["translation"]
        former_high = high
    return (min(former_low, low), max(former_high,high))

def overlap(stretch, start, end):
    if (stretch["start"] <= start and stretch["end"] >= start) or (stretch["end"] >= end and stretch["start"] <= end):
        return True
    return False

def get_new_range(possible):
    if len(possible) == 0:
        return None
    lows = [l[0] for l in possible]
    highs = [l[1] for l in possible]
    return min(lows), max(highs)

def get_min(seeds, pipeline):
    print("new")
    for f,pipe in enumerate(pipeline):
        possible = []
        for stretch in pipe:
            if not overlap(stretch, seeds[0], seeds[1]):
                continue
            possible.append(apply_pipe(seeds, stretch))
        ret = get_new_range(possible)
        if ret != None:
            seeds = ret
        print(list(range(seeds[0], seeds[1] + 1)))
    return seeds[0]

list_p = []
low = sum(seeds)
retval = []
for i in range(0, len(seeds), 2):
    r = []
    r.append(seeds[i])
    r.append(seeds[i] + seeds[i+1])
    retval.append(get_min(r, pipeline))

print(min(retval))

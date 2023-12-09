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

"""
seeds = [79, 14, 55, 13]
seeds = [79, 14]
pipes = [[[50, 98, 2], [52, 50, 48]],
        [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
        [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
        [[88, 18, 7], [18, 25, 70]],
        [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        [[0, 69, 1],[ 1, 0, 69]],
        [[ 60, 56, 37], [56, 93, 4]]]
        """

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

def apply_pipe(r, strech, mask):
    retval = []
    for idx, e in enumerate(r):
        if e >= stretch["start"] and e <= stretch["end"] and mask[idx] == False:
            e -= strech["translation"]
            mask[idx] = True
        retval.append(e)
    return (retval)

def overlap(stretch, start, end):
    if (stretch["start"] <= start and stretch["end"] >= start) or (stretch["end"] >= end and stretch["start"] <= end):
        return True
    return False

for i in range(0, len(seeds), 2):
    start = seeds[i]
    end = seeds[i+1] + seeds[i]
    r = list(range(start, end))
    start = r[0]
    end = r[-1]
    for f,pipe in enumerate(pipeline):
        start = r[0]
        end = r[-1]
        mask = [False for _ in range(len(r))]
        for stretch in pipe:
            if not overlap(stretch, start, end):
                continue
            r = apply_pipe(r, stretch, mask)
    seed = min(r)
    if seed < l:
        l = seed
print(l)

with open("input", "r") as f:
    content = f.read()

content = content.split("\n\n")

seeds = [int(x) for x in content[0].split(":")[1].split()]

content = content[1:]

pipes = []
l = max(seeds * 1000)
for t in content:
    pipe = t.split("\n")[1:]
    tmp = []
    for p in pipe:
        tmp.append([int(n) for n in p.split()])
    pipes.append(tmp)

"""
seeds = [79, 14, 55, 13]
pipes = [[[50, 98, 2], [52, 50, 48]], [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
        [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
        [[88, 18, 7], [18, 25, 70]],
        [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        [[0, 69, 1],[ 1, 0, 69],[ 60, 56, 37], [56, 93, 4]]]
"""

for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i] + seeds[i+1]):
        for pipe in pipes:
            for line in pipe:
                if (len(line) == 0):
                    continue
                if seed in range(line[1], line[1] + line[2]):
                    seed = seed - (line[1] - line[0])
                    break
                    #print(line[1], line[1] + line[2], line[0], seed)
        if seed < l:
            l = seed
print(l)



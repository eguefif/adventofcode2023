with open("input", "r") as f:
    content = f.read();

time, distance, _ = content.split("\n")
time = time.split(":")[1].strip()
distance = distance.split(":")[1].strip()
time = time.split()
distance = distance.split()

n = [0, 0, 0, 0]
for i in range(len(time)):
    for j in range(int(time[i])):
        dist = j * (int(time[i]) - j)
        if dist > int(distance[i]):
            n[i] += 1

print(n[0] * n[1] * n[2] * n[3])

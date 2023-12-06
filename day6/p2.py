with open("input", "r") as f:
    content = f.read();

time, distance, _ = content.split("\n")
time = time.split(":")[1].strip()
distance = distance.split(":")[1].strip()
time = time.split()
distance = distance.split()
time = int("".join(time))
distance = int("".join(distance))

print(time)
print(distance)

a = 0
for i in range(time):
    dist = i * (time - i)
    if dist > distance:
        a += 1
print(a)

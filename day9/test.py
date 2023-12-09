from math import comb

with open("input", "r") as f:
    content = f.read()

content = [c.split() for c in content.split('\n') if len(c) > 0]

data = []
for line in content:
    data.append([int(entry) for entry in line])

def Lagrange1(nums):
    n=len(nums)
    res=0
    for i,x in enumerate(nums):
        res+=x*comb(n,i)*(-1)**(n-1-i)
    return res

n = 0
for line in data:
    n += Lagrange1(line)
print(n)

t = int(input())
l = []

for i in range(t):
    l.append(int(input()))

l.sort()

for i in range(t):
    print(l[i])

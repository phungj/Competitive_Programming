n = int(input())

for _ in range(n):
    x = int(input())
    s = str(x) + " is even" if x % 2 == 0 else str(x) + " is odd"

    print(s)
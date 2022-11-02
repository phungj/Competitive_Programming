# Functions found from https://gist.github.com/paulhankin/c471b24c9a4717010681f0c5e33d6be9
def primes(n):
    x = [False] * (n + 1)
    for i in range(2, n + 1):
        if x[i]: continue
        yield i
        for j in range(2 * i, n + 1, i):
            x[j] = True


def prime_pairs(n):
    ps = list(primes(n))
    i, j = 0, len(ps) - 1
    while i <= j:
        while i <= j and ps[i] + ps[j] > n:
            j -= 1
        if i <= j and ps[i] + ps[j] == n:
            yield ps[i], ps[j]
        i += 1


n = int(input())

for _ in range(n):
    x = int(input())
    pairs = list(prime_pairs(x))

    print(str(x) + " has " + str(len(pairs)) + " representation(s)")

    for pair in pairs:
        print(str(pair[0]) + "+" + str(pair[1]))

    print()


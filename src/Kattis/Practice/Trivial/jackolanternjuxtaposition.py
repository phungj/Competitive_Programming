from operator import mul
from functools import reduce

params = input().split(" ")
params = [int(param) for param in params]

print(reduce(mul, params))

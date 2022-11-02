from itertools import tee
from math import pi
from time import perf_counter


# From https://stackoverflow.com/a/34562305
def pairwise(iterable):
    """
    s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = tee(iterable)
    next(b, None)

    return zip(a, b)


start = perf_counter()

for _ in range(int(input())):
    params = input().split(" ")
    params = [int(param) for param in params]
    angle = params[2] * 3600 + params[3] * 60 + params[4]
    current_angle = 0
    current_angle_diff = 0
    greatest_angle_diff = 0
    iterations = params[1] if params[1] < 360 * 3600 else 360 * 3600
    slices = [0] * iterations

    for i in range(len(slices)):
        current_angle = (current_angle + angle) % (360 * 3600)
        slices[i] = current_angle

    slices = sorted(list(set(slices)))
    slices.append(slices[0] + 360 * 3600)

    for pair in pairwise(slices):
        current_angle_diff = abs(pair[1] - pair[0])

        if current_angle_diff > greatest_angle_diff:
            greatest_angle_diff = current_angle_diff

    print((greatest_angle_diff / (360 * 3600)) * pi * params[0] ** 2)

print("\ndt:", perf_counter() - start)

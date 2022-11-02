from itertools import tee
from math import pi


# From https://stackoverflow.com/a/34562305
def pairwise(iterable):
    """
    s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = tee(iterable)
    next(b, None)

    return zip(a, b)


out = []

# There are 360 * 60 * 60 = 360 * 3600 seconds in a circle
for _ in range(int(input())):
    params = input().split(" ")
    params = [int(param) for param in params]
    angle = params[2] * 3600 + params[3] * 60 + params[4]
    current_angle = 0
    current_angle_diff = 0
    greatest_angle_diff = 0
    slices = set([])
    iterations = 0

    if (360 * 3600) % angle == 0:
        iterations = (360 * 3600) // angle

    for _ in range(min(iterations, params[1]) if iterations != 0 else min(params[1], 360 * 3600)):
        current_angle = (current_angle + angle) % (360 * 3600)
        slices.add(current_angle)

    slices = sorted(list(slices))
    slices.append(slices[0] + 360 * 3600)

    for pair in pairwise(slices):
        current_angle_diff = abs(pair[1] - pair[0])

        if current_angle_diff > greatest_angle_diff:
            greatest_angle_diff = current_angle_diff

    out.append(str((greatest_angle_diff / (360 * 3600)) * pi * params[0] ** 2))

print("\n".join(out))

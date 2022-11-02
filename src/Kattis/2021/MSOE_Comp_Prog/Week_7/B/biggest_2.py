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


for _ in range(int(input())):
    params = input().split(" ")
    params = [int(param) for param in params]
    angle = params[2] * 3600 + params[3] * 60 + params[4]
    last_angle = 0
    current_angle = 0
    greatest_angle_diff = 0
    # Ported from https://github.com/mxork/kattis/blob/master/biggest.c#L24
    slices = [False] * (360 * 3600)

    for i in range(params[1] if params[1] < 360 * 3600 else 360 * 3600):
        slices[(i * angle) % (360 * 3600)] = True

    for i in range(1, len(slices)):
        if slices[i] and i - last_angle > greatest_angle_diff:
            greatest_angle_diff = i - last_angle
            last_angle = i
        elif slices[i]:
            last_angle = i

    if 360 * 3600 - last_angle > greatest_angle_diff:
        greatest_angle_diff = 360 * 3600 - last_angle

    print(pi * (params[0] * params[0]) * (greatest_angle_diff / (360 * 3600)))

from scipy.spatial.distance import pdist
import numpy as np

class JunctionBox:
    def __init__(self, x, y, z, circuit=None):
        self._x = x
        self._y = y
        self._z = z
        self.circuit = circuit

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, JunctionBox):
            return False
        
        return self._x == value._x and self._y == value._y and self._z == value._z

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    split_lines = [line.split(',') for line in lines]
    points = [tuple(map(int, split_line)) for split_line in split_lines]

    pdists = pdist(points)

    print(np.argsort(pdists)[:1000])
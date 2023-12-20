import numpy as np

class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self._width = dim0
        self._height = dim1
        self._depth = dim2
        self._data = [0] * (dim0 * dim1 * dim2)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def depth(self):
        return self._depth

    def _get_index(self, x, y, z):
        return z * (self._width * self._height) + y * self._width + x

    def __getitem__(self, index):
        x, y, z = index
        if 0 <= x < self._width and 0 <= y < self._height and 0 <= z < self._depth:
            return self._data[self._get_index(x, y, z)]
        else:
            raise IndexError("Index out of range")

    # Методы для инкапсуляции данных

    def get_data(self):
        return self._data

    def set_data(self, data):
        if len(data) == self._width * self._height * self._depth:
            self._data = data
        else:
            raise ValueError("Invalid data length")

    def ones(self):
        self._data = [1] * (self._width * self._height * self._depth)

    def zeros(self):
        self._data = [0] * (self._width * self._height * self._depth)

    def fill(self, value):
        self._data = [value] * (self._width * self._height * self._depth)

    # Setter методы для инкапсуляции данных

    def set_width(self, width):
        if width >= 0:
            self._width = width
        else:
            raise ValueError("Width must be non-negative")

    def set_height(self, height):
        if height >= 0:
            self._height = height
        else:
            raise ValueError("Height must be non-negative")

    def set_depth(self, depth):
        if depth >= 0:
            self._depth = depth
        else:
            raise ValueError("Depth must be non-negative")

    def set_item(self, index, value):
        x, y, z = index
        if 0 <= x < self._width and 0 <= y < self._height and 0 <= z < self._depth:
            self._data[self._get_index(x, y, z)] = value
        else:
            raise IndexError("Index out of range")

    def set_values(self, values):
        if len(values) == self._width * self._height * self._depth:
            self._data = values
        else:
            raise ValueError("Invalid number of values")

# Добавляем методы для инкапсуляции данных

    def get_values0(self, i):
        if 0 <= i < self._width:
            return [self._data[self._get_index(i, y, z)] for y in range(self._height) for z in range(self._depth)]
        else:
            raise IndexError("Index out of range")

    def get_values1(self, j):
        if 0 <= j < self._height:
            return [self._data[self._get_index(x, j, z)] for x in range(self._width) for z in range(self._depth)]
        else:
            raise IndexError("Index out of range")

    def get_values2(self, k):
        if 0 <= k < self._depth:
            return [self._data[self._get_index(x, y, k)] for x in range(self._width) for y in range(self._height)]
        else:
            raise IndexError("Index out of range")

    def get_values01(self, i, j):
        if 0 <= i < self._width and 0 <= j < self._height:
            return [self._data[self._get_index(i, j, z)] for z in range(self._depth)]
        else:
            raise IndexError("Index out of range")

    def get_values02(self, i, k):
        if 0 <= i < self._width and 0 <= k < self._depth:
            return [self._data[self._get_index(i, y, k)] for y in range(self._height)]
        else:
            raise IndexError("Index out of range")

    def get_values12(self, j, k):
        if 0 <= j < self._height and 0 <= k < self._depth:
            return [self._data[self._get_index(x, j, k)] for x in range(self._width)]
        else:
            raise IndexError("Index out of range")

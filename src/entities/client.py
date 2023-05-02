class Client:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def asList(self):
        return [self.x, self.y]

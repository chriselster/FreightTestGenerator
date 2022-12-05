class Client:
    @staticmethod
    def header():
        return ['index', 'X_coordinate', 'Y_coordinate']

    def __init__(self, index, position, items):
        self.index = index
        self.position = position
        self.items = items

    def __str__(self):
        out = f'{self.index}, {self.position}, {len(self.items)}\n'
        for item in self.items:
            out += f'{item}\n'
        return out

    def asList(self):
        return [self.index] + self.position.asList()


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def asList(self):
        return [self.x, self.y]

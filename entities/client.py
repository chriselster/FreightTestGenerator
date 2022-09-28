class Client:
    def __init__(self, index, position, items):
        self.index = index
        self.position = position
        self.items = items

    def __str__(self):
        out = f'{self.index}, {self.position}, {len(self.items)}\n'
        for item in self.items:
            out += f'{item}\n'
        return out


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

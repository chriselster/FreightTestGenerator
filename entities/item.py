from random import randint, uniform


class Item:
    def __init__(self, id, destination):
        self.id = id
        self.weigth = round(uniform(1, 100), 2)
        self.type = randint(1, 10)
        self.position = destination

    def __str__(self):
        return f"{str(self.id)},{str(self.weigth)},{str(self.type)},{str(self.position.x)},{str(self.position.y)}"

class Quadrants:
    def __init__(self, _type):
        self.topLeft = False
        self.topRight = False
        self.bottomLeft = False
        self.bottomRight = False
        self.switchByType(_type)

    def switchByType(self, _type):
        match _type:
            case 1:
                self.topLeft = True
                self.topRight = True
                self.bottomLeft = True
                self.bottomRight = True

            case 2:
                self.topLeft = True
                self.topRight = True

            case 3:
                self.topRight = True
                self.bottomRight = True
            case 4:
                self.bottomRight = True
                self.bottomLeft = True

            case 5:
                self.bottomLeft = True
                self.topLeft = True

    def header(self):
        return ["topLeft", "topRight", "bottomLeft", "bottomRight"]

    def asList(self):
        return [self.topLeft, self.topRight, self.bottomLeft, self.bottomRight]

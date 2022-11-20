class Fares:
    @staticmethod
    def header():
        return ["type, fare"]

    def __init__(self, fares):
        self.fares = fares

    def asList(self):
        for i in self.fares:
            return [self.fares[i][0], self.fares[i][1]]

    def __eq__(self, other):
        return self.fares == other.fares

    # create hash
    def __hash__(self):
        return hash(tuple(self.fares))

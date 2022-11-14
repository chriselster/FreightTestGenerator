class Fares:
    def header(self):
        for i in range(1, len(self.fares) + 1):
            yield f"fareForType{i}"

    def __init__(self, fares):
        self.fares = fares

    def asList(self):
        return self.fares

    def __eq__(self, other):
        return self.fares == other.fares

    # create hash
    def __hash__(self):
        return hash(tuple(self.fares))

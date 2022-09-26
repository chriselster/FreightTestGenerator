class Carrier:
    def __init__(self,  veichles):
        self.veichles = veichles
        self.fare = 0

    def __str__(self):
        return ''.join(f"{str(veichle)}\n" for veichle in self.veichles) + "\n"

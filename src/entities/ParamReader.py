class ParamReader:
    def __init__(self, lines):
        self.lines = lines

    @staticmethod
    def getTokens(line):
        result = line.split(":")[1].split(",")
        result = [x.strip() for x in result]
        return [
            float(x) if "/" not in x else [float(y) for y in x[1:-1].split("/")]
            for x in result
        ]

    def next(self):
        if len(self.lines) == 0:
            return []

        line = self.lines.pop(0)
        return ParamReader.getTokens(line)

    def hasNext(self):
        return len(self.lines) > 0

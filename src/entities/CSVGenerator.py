class CSVGenerator:
    def generate(self, aClassList):
        return self.generate_header(aClassList) + self.generate_datarows(aClassList)

    def generate_header(self, aClassList):
        # Get class attributes
        aClass = aClassList[0]
        return ",".join(aClass.__dict__) + "\n"

    def generate_datarows(self, aClassList):
        return "".join([self.generate_datarow(aClass) for aClass in aClassList])

    def generate_datarow(self, aClass):
        return ",".join([str(attr) for attr in aClass.__dict__.values()]) + "\n"

class data():

    def __init__(self):
        self.starts = []

    def gemStart(self, income: list):
        if len(self.starts) != 0:
            for x in range(len(self.starts)):
                self.starts.pop(0)

        for x in range(len(income)):
            self.starts.insert(x, income[x])

    def getStart(self):
        return self.starts

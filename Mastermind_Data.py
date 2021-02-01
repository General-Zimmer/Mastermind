class data():

    def __init__(self):

        self.starts = []

    def gemStart(self, income: list):
        for x in range(len(income)):
            self.starts.insert(x, income[x])

    def getStart(self):
        return self.starts

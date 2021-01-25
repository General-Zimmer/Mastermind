class data():

    def __init__(self):

        self.starts = []

    def gemStart(self, income: tuple):
        for x in range(len(income)):
            self.starts.insert(x, income[x])

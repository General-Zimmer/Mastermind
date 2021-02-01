import Mastermind_Data as data


class dinLogik:

    def __init__(self):
        self.dat = data.data()

    def huskFarve(self):
        farver = []
        for x in range(4):
            farver.insert(x, input())
        print(farver)
        self.dat.gemStart(farver)

    def tjekFarve(self, get: list):
        rigtig = self.dat.getStart()
        for x in range(len(rigtig)):
            if rigtig[x] == get[x]:
                print("yes")
            else:
                print("no")

    def GenereFarve(self):
        pass




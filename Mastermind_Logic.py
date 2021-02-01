import Mastermind_Data as data


class dinLogik:

    def __init__(self):
        self.dat = data.data()

    def huskFarve(self, lst: list):
        farver = []
        for x in range(len(lst)):
            farver.insert(x, input())
        print(farver)
        self.dat.gemStart(farver)

    def tjekFarve(self, get: list):

        # Tjek farve, lav nummer. Tjek rigtig placering og farve, fjern farve
        svar = [0]
        farver = []
        len = len(self.dat.getStart())

        for x in range(len):
            if 1 == get.count(get[x]):
                farver.insert(get[x])

        for x in range(len):
            if rigtig[x] == get[x]:
                svar[0] = svar[0]+1
        return



    def GenereFarve(self):
        pass



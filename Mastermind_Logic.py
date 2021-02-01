import Mastermind_Data as data


class dinLogik:

    def __init__(self):
        self.dat = data.data()

    def huskFarve(self, lst: list):
        farver = []
        for x in range(len(lst)):
            farver.insert(x, lst[x])
        self.dat.gemStart(farver)

    def tjekFarve(self, get: list):

        svar = [0, 0]
        farver = []
        start = self.dat.getStart()
        lan = len(start)

        for x in range(lan):
            if 0 < get.count(start[x]) and farver.count(get[x]) == 0:
                farver.insert(x, get[x])
        print(farver)


        for x in range(len(farver)):

            if 0 != get.count(farver[x]):
                svar[1] = get.count(farver[x]) + svar[1]
                print(svar[1])

        for x in range(lan):
            if start[x] == get[x]:
                svar[0] = svar[0] + 1

        svar[1] = svar[1] - svar[0]
        return svar

    def GenereFarve(self):
        pass


geat = ["blå", "grøn", "blå", "rød", "lys blå"]
start = ["blå", "grøn", "blå", "røfa", "lygesgr"]
lo = dinLogik()
lo.huskFarve(start)
print(lo.dat.getStart())
print(lo.tjekFarve(geat))
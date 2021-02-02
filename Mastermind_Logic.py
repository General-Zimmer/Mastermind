import Mastermind_Data as data


class dinLogik:

    def __init__(self):
        self.dat = data.data()

    def huskFarve(self, lst: list):
        self.dat.gemStart(lst)

    def tjekFarve(self, get: list):

        svar = [0, 0]
        farver = []
        start = self.dat.getStart()
        lan = len(start)

        for x in range(lan):
            if 0 < start.count(get[x]) and farver.count(get[x]) == 0:
                farver.insert(x, get[x])

        for x in range(len(farver)):
            if 0 != get.count(farver[x]):
                svar[1] = get.count(farver[x]) + svar[1]

        for x in range(lan):
            if start[x] == get[x]:
                svar[0] = svar[0] + 1

        # Første tal er rigtig placering og farve, anden tal er kun rigtig farve
        svar[1] = svar[1] - svar[0]
        return svar


# geat = ["blå", "grøn", "blå", "rød", "lys blå"]
# start = ["blå", "grøn", "blå", "røfa", "lygesgr"]
# lo = dinLogik()
# lo.huskFarve(start)
# print(lo.tjekFarve(geat))

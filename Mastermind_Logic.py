import Mastermind_Data as data
import random


class dinLogik:

    def __init__(self):
        self.dat = data.data()
        self.trans = {
            0: "white",
            1: "purple",
            2: "Yellow",
            3: "dark blue",
            4: "dark red",
            5: "dark green"
        }

    def huskStart(self, lst=None):

        self.dat.gemStart(lst)

    def makeStart(self, num):
        lst = []
        for x in range(num):
            lst.insert(x, self.trans.get(random.randrange(6)))
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

    def RandColor(self):
        de = ("%02x" % random.randint(20, 255))
        re = ("%02x" % random.randint(20, 255))
        we = ("%02x" % random.randint(20, 255))
        ge = "#"
        color = ge + de + re + we
        return color
# geat = ["white", "dark green", "yellow", "dark blue"]
# start = ["blå", "grøn", "blå", "røfa", "lygesgr"]
# lo = dinLogik()
# lo.huskFarve(start)
# print(lo.tjekFarve(geat))

# lo.makeStart(4)

# print(lo.dat.getStart())

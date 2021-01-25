import Mastermind_Data

class dinmor:
    dict = {
        "blå": 0,
        "grøn": 1,
        "gul": 2,
    }

    def huskFarve(self):
        gæt = ["blå", "blå", "blå"]
        return gæt

    def tjekFarve(self, gæt : tuple, metode = huskFarve()):
        rigtig = metode()
        for x in range(len(rigtig)):
            if rigtig[x] == gæt[x]:
                print("yes")
            else:
                print("no")


    def GenereFarve(self):
        pass


gæt = ["blå", "grøn", "blå"]

dinmor().tjekFarve(gæt)


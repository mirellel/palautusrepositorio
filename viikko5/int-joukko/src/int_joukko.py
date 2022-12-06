KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):

        if luku in self.lukujono:
                return True
        return False

    def lisaa(self, luku):
        
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.lukujono):
                for i in range(self.kasvatuskoko):
                    self.lukujono.append([0])

    def poista(self, luku):
        if luku in self.lukujono:
            self.lukujono.remove(luku)
            self.alkioiden_lkm-=1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    def yhdiste(taulu1, taulu2):
        yhdiste = IntJoukko()
        taulu1 = taulu1.to_int_list()
        taulu2 = taulu2.to_int_list()

        for i in range(len(taulu1)):
            yhdiste.lisaa(taulu1[i])

        for i in range(len(taulu2)):
            yhdiste.lisaa(taulu2[i])

        return yhdiste


    def leikkaus(taulu1, taulu2):
        leikkaus = IntJoukko()
        taulu1 = taulu1.to_int_list()
        taulu2 = taulu2.to_int_list()

        for alkio in taulu1:
            if alkio in taulu2:
                leikkaus.lisaa(alkio)

        return leikkaus

    def erotus(taulu1, taulu2):
        erotus = IntJoukko()
        taulu1 = taulu1.to_int_list()
        taulu2 = taulu2.to_int_list()

        for i in taulu1:
            if i not in taulu2:
                erotus.lisaa(i)

        return erotus

    def __str__(self):
        tuotos = ""
        if self.alkioiden_lkm>0:
            for i in range(self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
        return "{"+tuotos+"}"

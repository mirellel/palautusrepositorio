from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavarat = 0
        for ostos in self.ostokset:
            tavarat += ostos.lukumaara()
        return tavarat

    def hinta(self):
        hinta = 0
        for ostos in self.ostokset:
            hinta += ostos.hinta()
        return hinta


    def lisaa_tuote(self, lisattava: Tuote):
        tuote = Ostos(lisattava)
        loytyy = False
        for ostos in self.ostokset:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                loytyy = True
        if not loytyy:
            self.ostokset.append(tuote)

    def poista_tuote(self, poistettava: Tuote):
        tuote = Ostos(poistettava)
        for ostos in self.ostokset:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)


    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostokset

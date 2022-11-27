import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_korin_hinta_yhden_tuotteen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavara(self):
        maito = Tuote("Maito", 3)
        bisse = Tuote("Olut", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_korin_hinta_kahden_eri_tuotteen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        bisse = Tuote("Olut", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavara(self):
        bisse = Tuote("Olut", 5)
        bisse = Tuote("Olut", 5)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_korin_hinta_kahden_saman_tuotteen_lisaamisen_jalkeen(self):
        bisse = Tuote("Olut", 5)
        bisse = Tuote("Olut", 5)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)

        self.assertEqual(self.kori.hinta(), 10)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset[0]
        nimi = ostos.tuotteen_nimi()
        maara = ostos.lukumaara()

        self.assertEqual((nimi, maara), ("Maito", 1))

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        maito = Tuote("Maito", 3)
        bisse = Tuote("Olut", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(bisse)

        ostokset = self.kori.ostokset

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset[0]
        nimi = ostos.tuotteen_nimi()
        maara = ostos.lukumaara()

        self.assertEqual((nimi, maara), ("Maito", 2))

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_toinen_poistetaan(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset[0]
        nimi = ostos.tuotteen_nimi()
        maara = ostos.lukumaara()

        self.assertEqual((nimi, maara), ("Maito", 1))

    def test_tuotteen_poistamisen_jalkeen_kori_on_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset
        hinta = self.kori.hinta()
        tavarat = self.kori.tavaroita_korissa()

        self.assertEqual((len(ostos), hinta, tavarat), (0, 0, 0))

    def test_ostoskorin_tyhjentaminen(self):
        maito = Tuote("Maito", 3)
        bisse = Tuote("Olut", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(bisse)

        self.kori.tyhjenna()

        ostokset = self.kori.ostokset

        self.assertEqual(len(ostokset), 0)
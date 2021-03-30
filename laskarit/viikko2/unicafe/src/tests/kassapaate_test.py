import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(640)

    def test_kassapaatteen_arvot_alussa_oikein(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat), (100000, 0, 0))

    def test_kateisosto_toimii_edullisissa_kun_maksu_on_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(241)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.edulliset), (100240, 1, 1))

    def test_kateisosto_toimii_maukkaissa_kun_maksu_on_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(401)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.maukkaat), (100400, 1, 1))

    def test_kateisosto_toimii_edullisissa_kun_maksu_ei_ole_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.edulliset), (100000, 239, 0))

    def test_kateisosto_toimii_maukkaissa_kun_maksu_ei_ole_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.maukkaat), (100000, 399, 0))

    def test_korttiosto_toimii_jos_rahaa_on_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat, str(self.maksukortti)), (100000, 1, 1, "saldo: 0.0"))

    def test_korttiosto_toimii_jos_rahaa_ei_ole_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat, str(self.maksukortti)), (100000, 1, 1, "saldo: 0.0"))

    def test_rahan_lataaminen_kortille_toimii_kun_summa_yli_0(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual((str(self.maksukortti), self.kassapaate.kassassa_rahaa), ("saldo: 7.4", 100100))
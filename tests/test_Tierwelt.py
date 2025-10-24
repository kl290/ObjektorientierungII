import unittest

from Tierwelt import Tier, Katze, Kuh, Schaf, Hund


class TestTierwelt(unittest.TestCase):

    def test_tier_name_korrekter_datentyp(self):
        tier = Tier("Bello")
        result = tier.info()
        self.assertEqual(result, "Das Tier heißt Bello.")

    def test_tier_name_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Tier(12)
        self.assertEqual(contextManager.exception.args[0], "Der Name muss ein nicht leerer String sein.")

    def test_tier_name_falscher_datentyp_v2(self):
        with self.assertRaises(ValueError) as contextManager:
            Tier("")
        self.assertEqual(contextManager.exception.args[0], "Der Name muss ein nicht leerer String sein.")

    def test_geraeusch_machen(self):
        tier = Tier("Bello")
        result = tier.geraeusch_machen()
        self.assertEqual(result, "Bello macht ein Geräusch.")

    def test_geraeusch_machen_katze(self):
        tier = Katze("Minka")
        result = tier.geraeusch_machen()
        self.assertEqual(result, "Minka miaut: Miau!")

    def test_geraeusch_machen_hund(self):
        tier = Hund("Bello")
        result = tier.geraeusch_machen()
        self.assertEqual(result, "Bello bellt: Wuff!")

    def test_geraeusch_machen_kuh(self):
        tier = Kuh("Lise")
        result = tier.geraeusch_machen()
        self.assertEqual(result, "Lise muht: Muh!")

    def test_geraeusch_machen_schaf(self):
        tier = Schaf("Olaf")
        result = tier.geraeusch_machen()
        self.assertEqual(result, "Olaf schreit: Mäh!")

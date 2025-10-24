import unittest

from Fahrzeuge import Fahrzeug, Auto, Elektroauto


class TestFahrzeuge(unittest.TestCase):

    def test_fahrzeug_korrekte_datentypen(self):
        fahrzeug = Fahrzeug("BMW", 2012)
        self.assertIsInstance(fahrzeug.marke, str)
        self.assertIsInstance(fahrzeug.baujahr, int)

    def test_auto_korrekte_datentypen(self):
        auto = Auto(322, "Benzin", "Mercedes", 2018)
        self.assertIsInstance(auto.ps, int)
        self.assertIsInstance(auto.kraftstoffart, str)

    def test_elektroauto_korrekter_datentyp(self):
        tesla = Elektroauto(82.5, 283, "Tesla Model 3", 2023)
        self.assertIsInstance(tesla.batteriekapazitaet, (int, float))

    def test_fahrzeug_marke_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Fahrzeug(2012, 2012)
        self.assertEqual(contextManager.exception.args[0], "Die Marke muss ein nicht leerer String sein.")

    def test_fahrzeug_marke_falscher_datentyp_v2(self):
        with self.assertRaises(ValueError) as contextManager:
            Fahrzeug(2012, "")
        self.assertEqual(contextManager.exception.args[0], "Die Marke muss ein nicht leerer String sein.")

    def test_fahrzeug_baujahr_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Fahrzeug("BMW", "Hallo")
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültiges Baujahr! Bitte eine ganze Zahl zwischen 1886 und 2025 angeben.")

    def test_fahrzeug_baujahr_ueberschreitung_der_obergrenze(self):
        with self.assertRaises(ValueError) as contextManager:
            Fahrzeug("BMW", 3000)
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültiges Baujahr! Bitte eine ganze Zahl zwischen 1886 und 2025 angeben.")

    def test_fahrzeug_baujahr_unterschreitung_der_untergrenze(self):
        with self.assertRaises(ValueError) as contextManager:
            Fahrzeug("BMW", 20)
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültiges Baujahr! Bitte eine ganze Zahl zwischen 1886 und 2025 angeben.")

    def test_info_fahrzeug(self):
        fahrzeug = Fahrzeug("BMW", 2012)
        result = fahrzeug.info()
        self.assertEqual(result, "BMW (2012)")

    def test_auto_ps_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Auto("", "Benzin", "Mercedes", 2018)
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültige PS-Angabe! Bitte eine positive ganze Zahl eingeben.")

    def test_auto_ps_groesser_0(self):
        with self.assertRaises(ValueError) as contextManager:
            Auto(0, "Benzin", "Mercedes", 2018)
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültige PS-Angabe! Bitte eine positive ganze Zahl eingeben.")

    def test_auto_kraftstoff_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Auto(322, 12, "Mercedes", 2018)
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültige Kraftstoffart! Bitte einen nicht-leeren Text eingeben.")

    def test_auto_kraftstoff_falscher_datentyp_v2(self):
        with self.assertRaises(ValueError) as contextManager:
            Auto(322, "", "Mercedes", 2018)
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültige Kraftstoffart! Bitte einen nicht-leeren Text eingeben.")

    def test_korrektes_auto(self):
        auto = Auto(300, "Benzin", "Mercedes", 2022)
        result = auto.info()
        self.assertEqual(result, "Mercedes (2022) -- 300 PS (Benzin)")

    def test_elektroauto_batteriekapazitaet_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Elektroauto("", 250, "Tesla", 2020)
        self.assertEqual(contextManager.exception.args[0],
                         "Ungültige Batteriekapazität! Bitte eine positive Zahl (int oder float) angeben.")

    def test_elektroauto_batteriekapazitaet_korrekter_datentyp(self):
        tesla = Elektroauto(82, 250, "Tesla", 2020)
        result = tesla.info()
        self.assertEqual(result, "Tesla (2020) -- 250 PS (elektrisch), Batteriekapazität: 82 kWh")

    def test_elektroauto_batteriekapazitaet_korrekter_datentyp_v2(self):
        tesla = Elektroauto(82.5, 250, "Tesla", 2020)
        result = tesla.info()
        self.assertEqual(result, "Tesla (2020) -- 250 PS (elektrisch), Batteriekapazität: 82.5 kWh")

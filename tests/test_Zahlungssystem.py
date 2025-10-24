import unittest
from unittest.mock import patch

from Zahlungssystem import Konto, Bargeldzahlung, Kreditkarte, PayPal


class TestZahlungssystem(unittest.TestCase):

    def test_konto_korrekte_datentypen(self):
        konto = Konto("Tom", 2400)
        self.assertIsInstance(konto.name, str)
        self.assertIsInstance(konto.kontostand, (int, float))

    def test_konto_name_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Konto(12, 2400)
        self.assertEqual(contextManager.exception.args[0], "Der 'name' muss ein nicht leerer String sein.")

    def test_konto_name_falscher_datentyp_v2(self):
        with self.assertRaises(ValueError) as contextManager:
            Konto("", 2400)
        self.assertEqual(contextManager.exception.args[0], "Der 'name' muss ein nicht leerer String sein.")

    def test_konto_kontostand_falscher_datentyp(self):
        with self.assertRaises(ValueError) as contextManager:
            Konto("Tom", "2400")
        self.assertEqual(contextManager.exception.args[0], "Der 'kontostand' muss eine Zahl größer als 0 sein.")

    def test_konto_kontostand_falscher_datentyp_v2(self):
        with self.assertRaises(ValueError) as contextManager:
            Konto("Tom", -500)
        self.assertEqual(contextManager.exception.args[0], "Der 'kontostand' muss eine Zahl größer als 0 sein.")

    def test_bargeldzahlung_transaktion(self):
        konto = Konto("Portemonnaie", 100)
        bargeld = Bargeldzahlung(20, konto)
        bargeld.transaktion_starten()
        self.assertEqual(konto.kontostand, 80)

    def test_paypal_transaktion(self):
        konto = Konto("PayPal", 1000)
        paypal = PayPal(110, "max.mustermann", konto)
        paypal.transaktion_starten()
        self.assertEqual(konto.kontostand, 890)

    def test_paypal_falscher_benutzername(self):
        konto = Konto("PayPal", 1000)
        with self.assertRaises(ValueError) as context:
            PayPal(50, "", konto)
        self.assertEqual(str(context.exception), "Der 'benutzername' muss ein nicht leerer String sein")

    def test_kreditkarte_transaktion(self):
        konto = Konto("Bankkonto", 5000)
        kreditkarte = Kreditkarte(600, 1000, konto)
        kreditkarte.transaktion_starten()
        self.assertEqual(konto.kontostand, 4400)

    def test_kreditkarte_falscher_kreditrahmen(self):
        konto = Konto("Bankkonto", 5000)
        with self.assertRaises(ValueError) as context:
            Kreditkarte(100, -50, konto)
        self.assertEqual(str(context.exception), "Der 'kreditrahmen' muss eine Zahl größer als 0 sein.")

    def test_zahlungssystem_falscher_betrag(self):
        konto = Konto("Bankkonto", 1000)
        with self.assertRaises(ValueError) as context:
            Bargeldzahlung(-10, konto)
        self.assertEqual(str(context.exception), "Der 'betrag' muss eine Zahl größer als 0 sein.")

    def test_zahlungssystem_falsche_waehrung(self):
        konto = Konto("Bankkonto", 1000)
        with self.assertRaises(ValueError) as context:
            Bargeldzahlung(10, konto, "")
        self.assertEqual(str(context.exception), "Die 'waehrung' muss ein nicht leerer String sein.")

    def test_zahlungssystem_falsches_kontoobjekt(self):
        with self.assertRaises(ValueError) as context:
            Bargeldzahlung(10, "Kein Konto")
        self.assertEqual(str(context.exception), "Die 'kontoinformation' muss ein Konto-Objekt sein.")

    @patch('builtins.print')
    def test_bargeldzahlung_betrag_hoeher_als_geld(self, mock_print):
        konto = Konto("Portemonnaie", 50)
        bargeld = Bargeldzahlung(100, konto)
        bargeld.transaktion_starten()
        mock_print.assert_any_call(
            "Fehler: Sie können die Zahlung: von 100 EUR nicht gewährleisten da sie nur 50 EUR zur Verfügung haben.")

    @patch('builtins.print')
    def test_paypal_betrag_hoeher_als_geld(self, mock_print):
        konto = Konto("PayPal", 50)
        paypal = PayPal(100, "max.mustermann", konto)
        paypal.transaktion_starten()
        mock_print.assert_any_call(
            "Fehler: Sie können die Zahlung: von 100 EUR nicht gewährleisten da sie nur 50 EUR zur Verfügung haben.")

    @patch('builtins.print')
    def test_kreditkarte_betrag_hoeher_als_geld(self, mock_print):
        konto = Konto("PayPal", 50)
        kreditkarte = Kreditkarte(100, 1000, konto)
        kreditkarte.transaktion_starten()
        mock_print.assert_any_call(
            "Fehler: Sie können die Zahlung: von 100 EUR nicht gewährleisten da sie nur 50 EUR zur Verfügung haben.")


if __name__ == "__main__":
    unittest.main()

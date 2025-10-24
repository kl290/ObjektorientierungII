from abc import ABC, abstractmethod


class Konto:

    def __init__(self, name, kontostand):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Der 'name' muss ein nicht leerer String sein.")
        self.name = name

        if not isinstance(kontostand, (int, float)) or kontostand <= 0:
            raise ValueError("Der 'kontostand' muss eine Zahl größer als 0 sein.")
        self.kontostand = kontostand


class Zahlungssystem(ABC):

    def __init__(self, betrag, kontoinformation, waehrung = "EUR"):
        if not isinstance(betrag, (int, float)) or betrag <= 0:
            raise ValueError("Der 'betrag' muss eine Zahl größer als 0 sein.")
        self.betrag = betrag

        if not isinstance(waehrung, str) or not waehrung.strip():
            raise ValueError("Die 'waehrung' muss ein nicht leerer String sein.")
        self.waehrung = waehrung

        if not isinstance(kontoinformation, Konto):
            raise ValueError("Die 'kontoinformation' muss ein Konto-Objekt sein.")
        self.kontoinformation = kontoinformation

        self.zahlungsmethode = None

    def transaktion_starten(self):
        print(f"Starte Zahlung: {self.betrag} {self.waehrung} mit {self.zahlungsmethode}.")
        self.zahlung_durchfuehren()
        self.bestaetigung_erstellen()
        print("Transaktion abgeschlossen.")
        print()

    def check_konto(self):
        if self.kontoinformation.kontostand >= self.betrag:
            self.kontoinformation.kontostand -= self.betrag
            return True
        else:
            print(
                f"Fehler: Sie können die Zahlung: von {self.betrag} {self.waehrung} nicht gewährleisten da sie nur {self.kontoinformation.kontostand} {self.waehrung} zur Verfügung haben.")
            return None

    @abstractmethod
    def zahlung_durchfuehren(self):
        pass # pragma no coverage

    @abstractmethod
    def bestaetigung_erstellen(self):
        pass # pragma no coverage


class Kreditkarte(Zahlungssystem):

    def __init__(self, betrag, kreditrahmen, kontoinformation, waehrung = "EUR"):
        super().__init__(betrag, kontoinformation, waehrung)
        if not isinstance(kreditrahmen, (int, float)) or kreditrahmen <= 0:
            raise ValueError("Der 'kreditrahmen' muss eine Zahl größer als 0 sein.")
        self.kreditrahmen = kreditrahmen

        self.zahlungsmethode = "Kreditkarte"

    def zahlung_durchfuehren(self):
        print("Kreditkarte wird belastet ...")
        if self.check_konto():
            print(f"Kreditrahmen reduziert. Neuer Kreditrahmen: {self.kontoinformation.kontostand} {self.waehrung}")

    def bestaetigung_erstellen(self):
        print("Transactions-ID: CC-4217")


class PayPal(Zahlungssystem):

    def __init__(self, betrag, benutzername, kontoinformation, waehrung = "EUR"):
        super().__init__(betrag, kontoinformation, waehrung)
        if not isinstance(benutzername, str) or not benutzername.strip():
            raise ValueError("Der 'benutzername' muss ein nicht leerer String sein")
        self.benutzername = benutzername

        self.zahlungsmethode = "PayPal"

    def zahlung_durchfuehren(self):
        print(f"{self.benutzername} wird zu PayPal weitergeleitet ...")
        if self.check_konto():
            print(f"PayPal-Guthaben nach Zahlung: {self.kontoinformation.kontostand} {self.waehrung}")

    def bestaetigung_erstellen(self):
        print("PayPal-Token: PP-98342")


class Bargeldzahlung(Zahlungssystem):

    def __init__(self, betrag, kontoinformation, waehrung = "EUR"):
        super().__init__(betrag, kontoinformation, waehrung)
        self.zahlungsmethode = "Bargeldzahlung"

    def zahlung_durchfuehren(self):
        print("Kunde bezahlt bar an der Kasse.")
        if self.check_konto():
            print(f"Neuer Bargeldbestand: {self.kontoinformation.kontostand} {self.waehrung}")

    def bestaetigung_erstellen(self):
        print("Quittung gedruckt.")

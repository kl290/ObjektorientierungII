class Tier:
    def __init__(self, name):  #
        self.name = name

    def geraeusch_machen(self):
        print(f"{self.name} macht ein Geräusch.")


class Hund(Tier):
    def geraeusch_machen(self):
        print(f"{self.name} bellt: Wuff!")


class Katze(Tier):
    def geraeusch_machen(self):
        print(f"{self.name} miaut: Miau!")


class Kuh(Tier):
    def geraeusch_machen(self):
        print(f"{self.name} muht: Muh!")


class Schaf(Tier):
    def geraeusch_machen(self):
        print(f"{self.name} schreit: Mäh!")


hund = Hund("Bello")
katze = Katze("Minka")
kuh = Kuh("Lise")
schaf = Schaf("Olaf")

hund.geraeusch_machen()
katze.geraeusch_machen()
kuh.geraeusch_machen()
schaf.geraeusch_machen()

# Wie könnte man so eine Anforderung, bei der jede Ableitung jeweils nur zwei Daten verwaltet
# (das Verb und das Geräusch), auch anders umsetzen? Mache einen Vorschlag, der die gleiche Ausgabe erzeugt.

# eine einzige Klasse mit Parameter:

class Tier:
    def __init__(self, name, verb, geraeusch):
        self.name = name
        self.verb = verb
        self.geraeusch = geraeusch

    def geraeusch_machen(self):
        print(f"{self.name} {self.verb}: {self.geraeusch}")


hund = Tier("Bello", "bellt", "Wuff!")
katze = Tier("Minka", "miaut", "Miau!")
kuh = Tier("Lise", "muht", "Muh!")
schaf = Tier("Olaf", "schreit", "Mäh!")

hund.geraeusch_machen()
katze.geraeusch_machen()
kuh.geraeusch_machen()
schaf.geraeusch_machen()
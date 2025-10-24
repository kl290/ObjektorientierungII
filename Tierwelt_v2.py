# Wie könnte man so eine Anforderung, bei der jede Ableitung jeweils nur zwei Daten verwaltet
# (das Verb und das Geräusch), auch anders umsetzen? Mache einen Vorschlag, der die gleiche Ausgabe erzeugt.

# eine einzige Klasse mit Parameter:

class Tier:
    def __init__(self, name, verb, geraeusch):
        if not isinstance((name, verb, geraeusch),
                          str) or not name.strip() or not verb.strip() or not geraeusch.strip():
            raise ValueError("Der 'Name' das 'Verb' und das 'Geraeusch' müssen ein nicht leerer String sein.")
        self.name = name
        self.verb = verb
        self.geraeusch = geraeusch

    def geraeusch_machen(self):
        print(f"{self.name} {self.verb}: {self.geraeusch}")

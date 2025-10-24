class Tier:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Der Name muss ein nicht leerer String sein.")
        self.name = name

    def info(self):
        return f"Das Tier heißt {self.name}."

    def geraeusch_machen(self):
        return f"{self.name} macht ein Geräusch."


class Hund(Tier):
    def geraeusch_machen(self):
        return f"{self.name} bellt: Wuff!"


class Katze(Tier):
    def geraeusch_machen(self):
        return f"{self.name} miaut: Miau!"


class Kuh(Tier):
    def geraeusch_machen(self):
        return f"{self.name} muht: Muh!"


class Schaf(Tier):
    def geraeusch_machen(self):
        return f"{self.name} schreit: Mäh!"

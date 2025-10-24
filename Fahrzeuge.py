class Fahrzeug:

    def __init__(self, marke, baujahr):
        if not isinstance(marke, str) or not marke.strip():
            raise ValueError("Die Marke muss ein nicht leerer String sein.")
        self.marke = marke

        if not isinstance(baujahr, int) or not (1886 <= baujahr <= 2025):
            raise ValueError("Ungültiges Baujahr! Bitte eine ganze Zahl zwischen 1886 und 2025 angeben.")
        self.baujahr = baujahr

    def info(self):
        return f"{self.marke} ({self.baujahr})"


class Auto(Fahrzeug):

    def __init__(self, ps, kraftstoffart, marke, baujahr):
        super().__init__(marke, baujahr)

        if not isinstance(ps, int) or ps <= 0:
            raise ValueError("Ungültige PS-Angabe! Bitte eine positive ganze Zahl eingeben.")
        self.ps = ps

        if not isinstance(kraftstoffart, str) or not kraftstoffart.strip():
            raise ValueError("Ungültige Kraftstoffart! Bitte einen nicht-leeren Text eingeben.")
        self.kraftstoffart = kraftstoffart

    def info(self):
        return f"{super().info()} -- {self.ps} PS ({self.kraftstoffart})"


class Elektroauto(Auto):
    def __init__(self, batteriekapazitaet, ps, marke, baujahr):
        super().__init__(ps, "elektrisch", marke, baujahr)

        if not isinstance(batteriekapazitaet, (int, float)) or batteriekapazitaet <= 0:
            raise ValueError("Ungültige Batteriekapazität! Bitte eine positive Zahl (int oder float) angeben.")
        self.batteriekapazitaet = batteriekapazitaet

    def info(self):
        return f"{super().info()}, Batteriekapazität: {self.batteriekapazitaet} kWh"

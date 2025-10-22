class Fahrzeug:

    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr

    def info(self):
        return f"{self.marke} ({self.baujahr})"


class Auto(Fahrzeug):
    def __init__(self, ps, kraftstoffart, marke, baujahr):
        super().__init__(marke, baujahr)
        self.ps = ps
        self.kraftstoffart = kraftstoffart

    def info(self):
        return f"{super().info()} -- {self.ps} PS ({self.kraftstoffart})"


class Elektroauto(Auto):
    def __init__(self, batteriekapazitaet, ps, marke, baujahr):
        super().__init__(ps, "elektrisch", marke, baujahr)
        self.batteriekapazitaet = batteriekapazitaet

    def info(self):
        return f"{super().info()}, Batteriekapazität: {self.batteriekapazitaet} kWh"


tesla1 = Elektroauto(82, 283, "Tesla Model 3", 2023)
auto2 = Auto(322, "Benzin", "Mercedes", 2018)
auto3 = Auto(75, "Benzin", "VW", 2002)
print(tesla1.info())
print(auto2.info())
print(auto3.info())

class ErrorTuliEtte(Exception):
    pass

class Inimene:

    def __init__(self, kaal, pikkus):
        self.kaal = kaal
        self.pikkus = pikkus

    def kmi(self):
        if self.kaal < 0 or self.pikkus < 0:
            raise ErrorTuliEtte
        return self.kaal/((self.pikkus/100)**2)

try:
    mari = Inimene(50,156)
    print(mari.kmi())
except ErrorTuliEtte:
    print("viga")



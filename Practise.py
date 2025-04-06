class Films:
    bestfilm = "BMB"

    def __init__(self, film1, film2, film3, film4):
        self.f1 = film1
        self.f2 = film2
        self.f3 = film3
        self.f4 = film4

    def print(self):
        return f"best films are {self.f1}, {self.f2}, {self.f3}, {self.f4}"

    @classmethod
    def change(cls, string):
        cls.bestfilm = string

    @classmethod
    def const(cls, string1):
        # params = string1.split("-")
        # return cls(params[0], params[1], params[2], params[3])
        return cls(*string1.split("-"))



A = Films("Prestige", "ZNMD", "Rockstar", "Tamasha")
print(A.print())

print(Films.bestfilm)

A.change("Bhaag")
print(A.bestfilm)
print(Films.bestfilm)

B = Films.const("abc-xyz-pqr-def")
print(B.print())
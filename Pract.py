class Country:
    BestCountry = "Norway"
    def __init__(self, C1, C2, C3, C4, C5):
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        self.C4 = C4
        self.C5 = C5

    def printdeets(self):
        return f"In order of Priority :- {self.C1}, {self.C2}, {self.C3}, {self.C4}, {self.C5}"

    @classmethod
    def change(cls, new):
        cls.BestCountry = new

    @classmethod
    def str(cls, strings):
        # params = strings.split("/")
        # return cls(params[0],params[1], params[2], params[3], params[4])
        return cls(*strings.split("/"))



Country1 = Country("USA", "Germany", "Canada", "Australia", "UK")
Country2 = Country("Florida", "Munich", "Vancouver", "Melbourne", "Leeds")

Country3 = Country.str("Spain/Maldives/Dubai/Sweden/France")
print(Country3.printdeets())


print(Country1.printdeets())
print(Country2.printdeets())

print(Country.BestCountry)

Country1.change("Switzerland")
print(Country2.BestCountry)

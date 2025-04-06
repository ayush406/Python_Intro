class Grandson:
    money = 78000

class Dad(Grandson):
    houses = 6
    var = 9
    def dan(self):
        return f"Yes I have {self.houses} houses."

class Son(Dad):
    houses = 9
    def dan(self):
        return f"Yes I have {self.houses} houses. I won"


tom = Grandson()
dick = Dad()
harry = Son()

print(harry.dan())
print(harry.var)
print(harry.money)
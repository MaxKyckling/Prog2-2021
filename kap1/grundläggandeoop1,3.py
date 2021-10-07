class Elev:
    def __init__(self, namn, age, godkand):
        self.namn = namn
        self.age = age
        if godkand == True:
            self.glad = True
        else:
            self.glad = False
        if not isinstance(namn, str):
            raise TypeError("Namnet måste vara en sträng")
        if not isinstance(age, int):
            raise TypeError("Åldern måste vara i heltal")

nibba = Elev("Albin",69)

class ImutableInteger:
    def __init__(self, number):
        self.__number = number  # Interní ukládání čísla
        self.imutable = True    # Výchozí hodnota: neměnitelné

    @property
    def number(self):
        return self.__number  # Návrat aktuální hodnoty

    @number.setter
    def number(self, new_number):
        if self.imutable:  # Pokud je imutable True, zablokuje změnu
            print("Změny nejsou povoleny!")
            return
        self.__number = new_number  # Nastavení nové hodnoty

    @property
    def imutable(self):
        return self.__imutable

    @imutable.setter
    def imutable(self, value):
        if not isinstance(value, bool):  # Kontrola, zda je hodnota boolean
            raise ValueError("Hodnota musí být typu bool (True nebo False).")
        self.__imutable = value


if __name__ == "__main__":
    ii = ImutableInteger(5)
    print(f"Počáteční hodnota: {ii.number}")

    ii.imutable = True  # Uzamčení změn
    ii.number = 60  # Pokus o změnu, která selže
    print(f"Po pokusu o změnu při uzamčení: {ii.number}")

    ii.imutable = False  # Odemčení změn
    ii.number = 60  # Úspěšná změna
    print(f"Po úspěšné změně: {ii.number}")

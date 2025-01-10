class Osoba:
    def __init__(self, jmeno, vek) -> None:
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self) -> str:
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"

class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik) -> None:
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self) -> str:
        return f"Student(jmeno={self.jmeno}, vek={self.vek}, rocnik={self.rocnik})"

class Ucitel(Osoba):
    def __init__(self, jmeno, vek, obor) -> None:
        super().__init__(jmeno, vek)
        self.obor = obor  # Opraven překlep

    def __str__(self) -> str:
        return f"Ucitel(jmeno={self.jmeno}, vek={self.vek}, obor={self.obor})"

if __name__ == "__main__":
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 19, 1)
    ucitel = Ucitel("Tomas", 40, "IT")

    print(student1)
    print(student2)
    print(ucitel)

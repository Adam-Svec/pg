# Funkce pro hledání největšího čísla v seznamu
def nejvetsi_cislo(seznam):
    if len(seznam) == 0:  # Pokud je seznam prázdný
        raise ValueError("Seznam nesmí být prázdný.")
    return max(seznam)  # Najde největší číslo v seznamu

# Testy pro funkci
def test_nejvetsi_cislo():
    assert nejvetsi_cislo([1, 2, 3, 4, 5]) == 5  # Testujeme seznam čísel
    assert nejvetsi_cislo([-1, -2, -3, -4]) == -1  # Testujeme záporná čísla
    assert nejvetsi_cislo([0]) == 0  # Testujeme seznam s jedním číslem

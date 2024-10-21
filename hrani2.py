def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False.
    """
    if cislo < 2:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Požádáme uživatele o zadání čísla
    try:
        cislo = int(input("Zadejte číslo: "))  # Přečteme číslo z terminálu
        if je_prvocislo(cislo):
            print(f"Číslo {cislo} je prvočíslo.")
        else:
            print(f"Číslo {cislo} není prvočíslo.")
    except ValueError:
        print("Zadejte platné číslo.")

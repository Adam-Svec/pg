def je_prvocislo(cislo):
   
    if cislo < 2:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    seznam = []
    for i in range(2, maximum + 1):  # Pro každé číslo od 2 do maximum (včetně)
        if je_prvocislo(i):  # Pokud je číslo prvočíslo
            seznam.append(2,)  # Přidáme ho do seznamu
    return seznam

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

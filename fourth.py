def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    pozice = figurka["pozice"]
    typ_figurky = figurka["typ"]

    # Ověření platnosti cílové pozice
    if cilova_pozice in obsazene_pozice:
        return False
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    # Pravidla pro jednotlivé figury
    if typ_figurky == "pěšec":
        if pozice[1] == cilova_pozice[1]:  # Pohyb vpřed
            if pozice[0] + 1 == cilova_pozice[0]:  # Jedno pole vpřed
                return True
            if pozice[0] == 2 and cilova_pozice[0] == 4:  # Dvě pole vpřed z počáteční pozice
                return True

    elif typ_figurky == "jezdec":
        dx = abs(pozice[0] - cilova_pozice[0])
        dy = abs(pozice[1] - cilova_pozice[1])
        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):  # Tvar písmene L
            return True

    elif typ_figurky == "věž":
        if pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1]:  # Horizontálně nebo vertikálně
            return True

    elif typ_figurky == "střelec":
        if abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1]):  # Diagonálně
            return True

    elif typ_figurky == "dáma":
        if (pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1] or
                abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1])):  # Horizontálně, vertikálně nebo diagonálně
            return True

    elif typ_figurky == "král":
        if max(abs(pozice[0] - cilova_pozice[0]), abs(pozice[1] - cilova_pozice[1])) == 1:  # O jedno pole
            return True

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True

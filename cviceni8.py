def obvod_ctverce(delka_strany):
    # funkce vypocita obvod ctverce z delky jeho strany
    return 4 * delka_strany

def obsah_ctverce(delka_strany):
    # funkce vypocita obsah ctverce z delky jeho strany
    return delka_strany ** 2

def pocet_pismen(text, pismeno):
    return text.lower().count(pismeno.lower())


def index_pismene(text,pismeno):
   return [i for i, char in enumerate(text) if char.lower() == pismeno.lower()]

def fibomachi(maximum):
    posloupnost = [1, 1]  # Začínáme s prvními dvěma čísly
    while posloupnost[-1] + posloupnost[-2] <= maximum:
        nove_cislo = posloupnost[-1] + posloupnost[-2]  # Součet posledních dvou čísel
        posloupnost.append(nove_cislo)  # Přidáme nové číslo do posloupnosti
    return posloupnost

    

if __name__ == "__main__":
    print(obsah_ctverce(4))  
    print(obsah_ctverce(5))  

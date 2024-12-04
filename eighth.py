def bin_to_dec(binarni_cislo):
    # Převedení vstupu na řetězec, podpora jak int, tak str
    if isinstance(binarni_cislo, int):
        bin_str = str(binarni_cislo)
    elif isinstance(binarni_cislo, str):
        bin_str = binarni_cislo
    else:
        raise ValueError("Vstup musí být celé číslo nebo řetězec.")
    
    # Ověření, zda obsahuje pouze 0 a 1
    if not all(c in '01' for c in bin_str):
        raise ValueError("Vstupní binární číslo může obsahovat pouze '0' a '1'.")
    
    # Ruční výpočet hodnoty
    vysledek = 0
    for i, bit in enumerate(reversed(bin_str)):
        if bit == '1':
            vysledek += 2 ** i
    return vysledek

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    

if __name__ == "__main__":
    # Test konkrétních čísel
    print(f"10011101 -> {bin_to_dec('10011101')}")  # Mělo by vypsat 157
    print(f"010101 -> {bin_to_dec('010101')}")  # Mělo by vypsat 21
    
    # Spuštění testů
    test_funkce()
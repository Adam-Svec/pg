def dec_to_bin(cislo):
    # Převedení vstupního čísla na integer, pokud je to řetězec
    cislo = int(cislo)
    
    # Speciální případ pro 0
    if cislo == 0:
        return "0"
    
    # Inicializace prázdného řetězce pro binární reprezentaci
    binary = ""
    
    # Iterativní převod čísla na binární reprezentaci
    while cislo > 0:
        # Přidání zbytku po dělení 2 na začátek řetězce
        binary = str(cislo % 2) + binary
        # Celočíselné dělení 2
        cislo //= 2
    
    return binary

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
    assert dec_to_bin(167) == "10100111"  # Přidán test pro 167
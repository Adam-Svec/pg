# eighth.py
def bin_to_dec(binarni_cislo):
    # Funkce spočítá hodnotu předávaného binárního čísla
    # binarni_cislo může být str i int!!!
    if isinstance(binarni_cislo, int):
        bin_str = str(binarni_cislo)
    elif isinstance(binarni_cislo, str):
        bin_str = binarni_cislo
    else:
        raise ValueError("Vstup musí být celé číslo nebo řetězec.")
    
    if not all(c in '01' for c in bin_str):
        raise ValueError("Vstupní binární číslo může obsahovat pouze '0' a '1'.")
    
    return int(bin_str, 2)


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157  # Binární číslo 10011101 = 157
    assert bin_to_dec("10100111") == 167  # Binární číslo 10100111 = 167
    print("Všechny testy proběhly úspěšně.")

# Spuštění testů
test_bin_to_dec()

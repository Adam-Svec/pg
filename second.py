def cislo_text(cislo):
    
    cislo = int(cislo)

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    specialni_cisla = {
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct",
        15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct",
        100: "sto"
    }

    
    if cislo in specialni_cisla:
        return specialni_cisla[cislo]

   
    if cislo < 10:
        return jednotky[cislo]

    
    if cislo < 100:
        desitka = desitky[cislo // 10]
        jednotka = jednotky[cislo % 10]
        if cislo % 10 == 0:
            return desitka  
        return f"{desitka} {jednotka}"  

    return "Neplatné číslo"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
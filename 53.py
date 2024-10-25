from hrani import jaccardova_vzdalenost_mnozin
from hrani2 import levensteinova_vzdalenost

def deduplikace_dotazu(dotazy):
    """
    Tato funkce spočítá Jaccardovu vzdálenost a Levenshteinovu vzdálenost a vyřadí z 
    seznamu dotazy, položky, které budou mít Jaccardovu vzdálenost menší než 0.5 
    a Levenshteinovu vzdálenost <= 1.
    """
    jedine_dotazy = []
    i = 0

    while i < len(dotazy):
        je_duplikat = False
        j = 0

        while j < len(jedine_dotazy):
            jaccard_vzdalenost = jaccardova_vzdalenost_mnozin(dotazy[i]['serp'], jedine_dotazy[j]['serp'])
            levenstein_vzdalenost = levensteinova_vzdalenost(dotazy[i]['dotaz'], jedine_dotazy[j]['dotaz'])

            if jaccard_vzdalenost < 0.5 and levenstein_vzdalenost <= 1:
                je_duplikat = True
                break  # Pokud najdeme duplikát, přerušíme vnitřní cyklus
            j += 1  # Zvyšujeme index j

        if not je_duplikat:
            jedine_dotazy.append(dotazy[i])  # Přidáme dotaz, pokud není duplikát
        i += 1  # Zvyšujeme index i

    return jedine_dotazy

if __name__ == "__main__":
    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    print(deduplikace_dotazu([dotaz1, dotaz2, dotaz3]))

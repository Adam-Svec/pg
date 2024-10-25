def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):
    set1 = set(mnozina1)
    set2 = set(mnozina2)

    prunik = set1.intersection(set2)
    sjednoceni = set1.union(set2)

    jaccarduv_index = len(prunik) / len(sjednoceni)
    jaccardova_vzdalenost = 1 - jaccarduv_index

    return jaccardova_vzdalenost

if __name__ == "__main__":
    serp1 = ["https://www.seznam.cz", "https://www.google.com", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    serp2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    serp3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

    print(jaccardova_vzdalenost_mnozin(serp1, serp2))
    print(jaccardova_vzdalenost_mnozin(serp2, serp3))
    print(jaccardova_vzdalenost_mnozin(serp1, serp3))
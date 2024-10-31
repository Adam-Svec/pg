import sys
import csv

def nacti_csv(soubor):
    data = []
    with open(soubor, "r") as file:
        reader = csv.reader(file)
        for radek in reader:
            data.append(radek)
    return data

def  zapis_csv(soubor, data):
    with open(soubor, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)


        
if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        print(csv_data1, csv_data2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        zapis_csv(vysledna_data)
    except Exception:
        print("zadaej 2 vstupni soubory csv")
    except FileNotFoundError:
        print("soubor existuje")
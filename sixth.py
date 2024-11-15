import sys
import requests
from bs4 import BeautifulSoup

def stahni_url_a_ziskej_vsechny_href(url):
    """
    Funkce stáhne URL zadanou v parametru `url` pomocí volání `response = requests.get()`.
    Zkontroluje návratový kód `response.status_code`, který musí být 200.
    Pokud je kód 200, najde ve staženém obsahu stránky (`response.content`) všechny výskyty
    <a href="url">odkaz</a> a z nich načte URL, která vrátí jako seznam pomocí `return`.
    """
    try:
        odpoved = requests.get(url)  # Stáhnutí obsahu URL
        if odpoved.status_code == 200:
            soup = BeautifulSoup(odpoved.content, "html.parser")
            odkazy = [odkaz.get("href") for odkaz in soup.find_all("a")]
            return odkazy
        else:
            return []  # Pokud není návratový kód 200, vrátí prázdný seznam
    except requests.exceptions.RequestException as chyba:
        print(f"Chyba při stahování URL: {chyba}")
        return []

if __name__ == "__main__":
    try:
        # Načtení URL z příkazového řádku
        url = sys.argv[1]
        vsechny_odkazy = stahni_url_a_ziskej_vsechny_href(url)
        
        if vsechny_odkazy:
            print("Odkazy:")  # Zobrazení nadpisu "Odkazy:"
            for odkaz in vsechny_odkazy:
                if odkaz:  # Kontrola, že odkaz není None
                    print(odkaz)
        else:
            print("Žádné odkazy nebyly nalezeny.")
    except IndexError:
        print("Zadejte prosím URL jako parametr při spuštění programu.")
    except Exception as chyba:
        print(f"Program skončil chybou: {chyba}")

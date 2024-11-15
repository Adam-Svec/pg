import requests
from bs4 import BeautifulSoup

def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"Nastala chyba, nepodařilo se připojit: {url}")
        return nadpisy  

    if response.status_code != 200:
        print(f"Nastala chyba, HTTP kód: {response.status_code}")
        return nadpisy  

    
    soup = BeautifulSoup(response.text, 'html.parser')

   
    for nadpis in soup.find_all('h1'):
        nadpisy.append(nadpis.text.strip())

    return nadpisy

if __name__ == "__main__":
    url = input("Zadej URL: ")
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    print("Nalezené nadpisy h1 na stránce:")
    for nadpis in nadpisy:
        print(nadpis)

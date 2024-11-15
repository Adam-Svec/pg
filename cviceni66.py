import json
import requests

url = "https://db.carnewschina.com/suggest?q="

def download_json_and_parse_brands(prefix):
    # Stáhneme data z URL s připojeným prefixem
    response = requests.get(url + prefix)
    
    # Kontrola, zda je požadavek úspěšný
    if response.status_code != 200:
        print(f"Chyba: HTTP kód {response.status_code}")
        return []
    
    # Načteme JSON data
    json_data = response.json()
    
    brands = []
    
    # Projít JSON data a extrahovat názvy značek
    for item in json_data.get("brands", []):
        brands.append(item["name"])
    
    return brands

if __name__ == "__main__":
    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    print("Nalezené značky:")
    for brand in brands:
        print(brand)


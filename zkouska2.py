import requests
from unittest.mock import patch, MagicMock


def convert_to_czk(amount, currency):
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    
   
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Unable to fetch exchange rates.")
    

    data = response.text.splitlines()

    
    for line in data:
        columns = line.split("|")
        
        
        if len(columns) > 4:
            currency_code = columns[3].strip()
            if currency_code == currency:
               
                rate = columns[4].replace(",", ".").strip()
                return round(amount * float(rate), 2)
    
    
    raise ValueError(f"Currency {currency} not found in the exchange rate list.")


def test_convert_to_czk():
   
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    
    with patch("requests.get") as mock_get:
        
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        
        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."


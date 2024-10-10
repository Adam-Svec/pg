# funkce vrati treti prvek ze seznamu
#def vrat_treti(seznam):
    #if len(seznam) <=3:
      #  return None
    #else:
     #   return seznam[2]
         

# funkce spocita prumer z hodnot v seznamu


# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(student):
    jmeno = student["jmeno"]
    prijmeni = student["prijmeni"]
    vek = student["vek"]
    prumer = round(sum(student["znamky"])/len(student["znamky"]),1)
    return f"Jmeno {jmeno}, prijmeni {prijmeni}, vek {vek}, prumer {prumer}"
    


if __name__ == "__main__":
  #  print(vrat_treti([9,8,7]))
   


    
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))
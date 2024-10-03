
#
def stars_while():
    print("zacatek")

    i = 0

    while i<5:
        print("*")
        i += 1
    print("konec")

#    
def stars_while():
    print("zacatek")

    for i in range(5):
        print("*", i)

    print("konec")    

# funkce urcujci, zda number lezi mezi min_number a max_number
def in_range(min_number, max_number, number):
    if number >= min_number and number <= max_number:
        print("is in range")
    else:
        print("is not in rage")

#in_range(100, 1000, 2000)


#funkce vypise string "Ahoj jmeno"
def dopln_jmeno(jmeno):
    print("ahoj",jmeno)

jm = input("Zadej jmeno: ")

#print (jm)
dopln_jmeno(jm)
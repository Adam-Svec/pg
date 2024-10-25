def levensteinova_vzdalenost(dotaz1, dotaz2):
   
    if len(dotaz1) == 0:
        return len(dotaz2)
    elif len(dotaz2) == 0:
        return len(dotaz1)
    else:
   
        if dotaz1[-1] == dotaz2[-1]:
            return levensteinova_vzdalenost(dotaz1[:-1], dotaz2[:-1])
        else:
           
            return 1 + min(
                levensteinova_vzdalenost(dotaz1, dotaz2[:-1]),  
                levensteinova_vzdalenost(dotaz1[:-1], dotaz2),  
                levensteinova_vzdalenost(dotaz1[:-1], dotaz2[:-1]))  


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))
from cviceni8 import obsah_ctverce,obvod_ctverce,pocet_pismen,index_pismene


def test_obsah_ctverce():
    assert obsah_ctverce(4) == 16
    assert obsah_ctverce(5) == 25

def test_obvod_ctverce():
    assert obvod_ctverce(4) == 16
    assert obvod_ctverce(5) == 20


def test_pocet_pismen():
    assert pocet_pismen("Ahoj jak se mas?","a") == 3
    assert pocet_pismen("Ahoj jak se mas?","j") == 2

    
def fibomachi(maximum):
    return  fibomachi(5) == [1,1,2,3,5]
    return  fibomachi(10) == [1,1,2,3,5,8]
def test_inde_pismen():
    assert index_pismene("Ahoj, jak se mas?", "a") == [0,7,14]
    assert index_pismene("Ahoj, jak se mas?", "x") == []
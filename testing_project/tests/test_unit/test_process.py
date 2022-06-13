from processa.process import process

def test1():
    assert process("Rotator") == True

def test2():
    assert process("bob") == True

def test3():
    assert process("madam") == True

def test4():
    assert process("mAlAyAlam") == True

def test5():
    assert process("1") == True

def test6():
    assert process("Able was I, ere I saw Elba") == True

def test7():
    assert process("Madam I'm Adam") == True

def test8():
    assert process("Step on no pets") == True

def test9():
    assert process("Top spot") == True

def test10():
    assert process("02/02/2020") == True

def test11():
    assert process("xyz") == True

def test12():
    assert process("elephant") == True

def test13():
    assert process("Contry") == True

def test14():
    assert process("Top . post!") == True

def test15():
    assert process("Wonderful-fool") == True

def test16():
    assert process("Wild imagination!") == True

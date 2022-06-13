def process(a):

    b = ''.join(char for char in a if char.isalnum())

    if str(b.lower()) == ''.join(reversed(b.lower())) :
        lRet = True
    else:
        lRet = False

    return lRet
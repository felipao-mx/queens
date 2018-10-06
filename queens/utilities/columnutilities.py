
def numToString(num):
    if num <= 0 or num > 27:
        raise ValueError()

    return str(chr(num + 96)).upper()

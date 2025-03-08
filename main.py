def isOdd(input: int) -> bool:
    if input == 0:
        return False
    elif input == 1:
        return True
    elif input == 2:
        return False
    elif input == 3:
        return True
    elif input == 4:
        return False
    elif input == 5:
        return True
    elif input == 6:
        return False
    elif input == 7:
        return True
    elif input == 8:
        return False
    elif input == 9:
        return True
    elif input == 10:
        return False
    elif input == 11: # fix for pineafan. program required up to 11
        return True
    else:
        raise ValueError("I do not know. Please submit an issue report.")


def isntOdd(input: int) -> bool:
    isAnOddNumber = isOdd(input)
    if isAnOddNumber:
        return False
    else:
        return True


def HelloWorld(input: str) -> None:
    print(input)

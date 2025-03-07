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
    else:
        # Oh, no! This number doesn't work! What do I do with it?
        数 = process_input(input)
        # Let's take 10 away from this number...
        数 -= 10
        # ...and try again!
        return isOdd(数)

def process_input(input: int):
    # We have to account for negative numbers
    if input < 0:
        return abs(input)
    elif input > 0:
        return input
    elif input == 0:
        return input * (10 ** 69)
    else:
        raise ValueError("How did we get here?")

def isntOdd(input: int) -> bool:
    isAnOddNumber = isOdd(input)
    if isAnOddNumber:
        return False
    else:
        return True


def HelloWorld(input: str) -> None:
    print(input)

import sys

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

def print(data):
    def console_write(index):
        if index >= len(data):
            # there's no more data to write! :O
            sys.stdout.write("\n")
            sys.stdout.flush()
            return
        # send the bite :D
        sys.stdout.write(data[index])
        sys.stdout.flush()
        # yay next bite :3
        console_write(index + 1)
    
    # Start writing!
    console_write(0)

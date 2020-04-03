'''

1-BIT and 2-BIT CHARACTERS

We have two special characters. The first character can be represented by one bit 0. 
The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. 
The given string will always end with a zero.

'''

def isOneBitCharacter(bits: List[int]) -> bool:
    if not bits:
        return True
    i = 0
    while i < len(bits)-1:
        if bits[i] is 1:
            i += 2
        else:
            i += 1

    return i == len(bits)-1

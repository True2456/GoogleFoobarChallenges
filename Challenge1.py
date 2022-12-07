BRAILLE_DICT = {
    "a": "100000",
    "b": "110000",
    "c": "100100",
    "d": "100110",
    "e": "100010",
    "f": "110100",
    "g": "110110",
    "h": "110010",
    "i": "010100",
    "j": "010110",
    "k": "101000",
    "l": "111000",
    "m": "101100",
    "n": "101110",
    "o": "101010",
    "p": "111100",
    "q": "111110",
    "r": "111010",
    "s": "011100",
    "t": "011110",
    "u": "101001",
    "v": "111001",
    "w": "010111",
    "x": "101101",
    "y": "101111",
    "z": "101011",
    " ": "000000",
}

def solutions(s):
    answer = ""
    try:
        for char in s:
            if char.isupper():
                answer = answer + "000001"
                answer = answer + BRAILLE_DICT.get(char.lower())
            else:
                answer = answer + BRAILLE_DICT.get(char.lower())
    except:
        print("invalid input according to specifications")
    return answer


def test1():
    assert solutions("code") == "100100101010100110100010", "Result Should be 100100101010100110100010"

def test2():
    assert solutions("Braille") == "000001110000111010100000010100111000111000100010", "Result should be 000001110000111010100000010100111000111000100010"

def test3():
    assert solutions("The quick brown fox jumps over the lazy dog") == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110", "Result should be 000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
print(solutions("Braille"))
test1()
print("Test 1 Passed \n")
print(solutions("code"))
test2()
print("Test 2 Passed \n")
print(solutions("Braille"))
test3()
print("Test 3 Passed \n")
print(solutions("Braille"))

"""
Numerology Calculator Package:

Destiny number from your name or initial.
Soul Urge number from your vowels.
Personality number from your consonants.
Life path number from your birthdate.
"""


def main():
    while True:
        name = input("Enter your name or initial: ")
        birthdate = input("Enter your birthdate in (mm/dd/yyyy) format: ")
        print("Name Number (Destiny Number)")
        numerology_chart(name)

        print("Soul Urge Number")
        soul_urge_numerology(name)

        print("Personality Number")
        numerology_personality(name)

        print("Life Path Number")
        numerology_birthdate(birthdate)
        exit = input("Press [x + Enter] to exit or [Enter] to continue: ")
        if exit.upper() == 'X':
            break



def numerology_chart(name):
    total = 0
    numerology = 0
    for char in name.upper():
        if char == "A" or char == "J" or char == "S":
            total += 1
        elif char == "B" or char == "K" or char == "T":
            total += 2
        elif char == "C" or char == "L" or char == "U":
            total += 3
        elif char == "D" or char == "M" or char == "V":
            total += 4
        elif char == "E" or char == "N" or char == "W":
            total += 5
        elif char == "F" or char == "O" or char == "X":
            total += 6
        elif char == "G" or char == "P" or char == "Y":
            total += 7
        elif char == "H" or char == "Q" or char == "Z":
            total += 8
        elif char == "I" or char == "R":
            total += 9
    total = str(total)
    for numr in total:
        numr = int(numr)
        numerology += numr
    print(numerology)
    
def soul_urge_numerology(name):
    total = 0
    numerology = 0
    for char in name.upper():
        if char == "A":
            total += 1
        elif char == "U":
            total += 3
        elif char == "E":
            total += 5
        elif char == "O":
            total += 6
        elif char == "I":
            total += 9
    total = str(total)
    for numr in total:
        numr = int(numr)
        numerology += numr
    print(numerology)

def numerology_personality(name):
    total = 0
    numerology = 0
    for char in name.upper():
        if char == "J" or char == "S":
            total += 1
        elif char == "B" or char == "K" or char == "T":
            total += 2
        elif char == "C" or char == "L":
            total += 3
        elif char == "D" or char == "M" or char == "V":
            total += 4
        elif char == "N" or char == "W":
            total += 5
        elif char == "F" or char == "X":
            total += 6
        elif char == "G" or char == "P" or char == "Y":
            total += 7
        elif char == "H" or char == "Q" or char == "Z":
            total += 8
        elif char == "R":
            total += 9
    total = str(total)
    for numr in total:
        numr = int(numr)
        numerology += numr
    print(numerology)
    

def numerology_birthdate(birthdate):
    total = 0
    demiliter = "/"
    numerology = 0

    temp = birthdate.split(demiliter)
    number = "".join(temp)
    for num in number:
        num = int(num)
        total += num
    total = str(total)
    for numr in total:
        numr = int(numr)
        numerology += numr
    print(numerology)
    


if __name__ == "__main__":
    main()
def get_word():
    return input("Enter word:")


samogloski = ["a", "o", "e", "i", "u"]


def samo(word):
    for i in word:
        if i in samogloski:
            return False
    return True


def samoNum(word):
    suma = 0
    for i in word:
        if i in samogloski:
            suma += 1
    return suma


word = get_word()

while not samo(word):
    print(samoNum(word))

    word = get_word()

print(word)
import random
def play():

    print_welcome()
    secret_word = load_secret_word()
    correct_letters = initialize_letters_successful(secret_word)
    print(correct_letters)

    hanged = False
    successful = False
    errors = 0

    while(not hanged and not successful):

        kick = ask_kick()

        if(kick in secret_word):
            mark_correct_kick(kick, correct_letters, secret_word)
        else:
            errors += 1

        hanged = errors == 6
        successful = "_" not in correct_letters
        print(correct_letters)

    if(successful):
        print_winner_message()
    else:
        print_message_loser()


def print_welcome():
    print("***************")
    print("Bem vindo ao jogo da Forca")
    print("***************")

def load_secret_word():
    file = open("palavras.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

def initialize_letters_successful(word):
    return ["_" for letra in word]

def ask_kick():
    kick = input("Digite sua letra: ")
    kick = kick.strip().upper()
    return kick

def mark_correct_kick(kick, correct_letters, secret_word):
    index = 0
    for letra in secret_word:
        if (kick.upper() == letra.upper()):
            correct_letters[index] = letra
        index += 1
def print_winner_message():
    print("Parabéns! Você ganhou")

def print_message_loser():
    print("Lamento, mas você perdeu, tente novamente")

if(__name__ == "__main__"):
    play()

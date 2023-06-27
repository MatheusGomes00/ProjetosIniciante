import random


def print_opening_message(opt):
    if opt == 'hangman':
        print('*******************************')
        print('***Welcome to the hangman game!***')
        print('*******************************')
    elif opt == 'guessing':
        print('***********************')
        print('*    Jogo da adivinhação     *')
        print('***********************')
        print("Você terá 5 chances para acertar o número.")
    elif opt == 'menu':
        print("*********************")
        print("****MENU DE JOGOS****")
        print("*********************")
        print("1. Guessing")
        print("2. Hangman")


def load_secret_word():
    arquivo = open('words.txt', 'r')
    words = []
    for line in arquivo:
        line = line.strip()
        words.append(line)
    arquivo.close()
    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def initialize_right_letters(secret_word):
    return ['_' for letter in secret_word]


def asks_guess():
    guess = input('Which letter?    ')
    guess = guess.strip().upper()
    return guess


def mark_right_guess(secret_word, guess, right_letters):
    position = 0
    for letter in secret_word:
        if guess.upper() == letter.upper():
            print(f'Found the letter {letter.upper()} in position {position}')
            right_letters[position] = letter.upper()
        position += 1


def hangman():
    print_opening_message('hangman')
    secret_word = load_secret_word()
    right_letters = initialize_right_letters(secret_word)
    hit = False
    hanged = False
    mistakes = 0
    wrong_letters = []
    while not hit and not hanged:
        if wrong_letters:
            print(f'Wrong letters\n{wrong_letters}')

        print(right_letters)

        guess = asks_guess()
        if guess in secret_word:
            mark_right_guess(secret_word, guess, right_letters)
        else:
            mistakes += 1
            wrong_letters.append(guess)

        hit = '_' not in right_letters
        hanged = mistakes == 6

    if hit:
        print('You hit the right word!!')
    else:
        print('You lose!!\nHanged.')

    print('End Game!')


def guessing():
    print_opening_message('guessing')
    turn = 1
    n_random = random.randrange(0, 10)
    print(n_random)
    guess = int(input("Entre com um número inteiro de 0 a 10:    "))

    while turn <= 5:
        print(f"Tentativa {turn} de 5\n")
        if guess == n_random:
            print("Acertou!!!")
            break
        elif guess > n_random:
            print("Você errou!!! O seu chute foi maior que o número secreto")
        elif guess < n_random:
            print("Você errou!!! O seu chute foi menor que o número secreto")
        if turn == 5 and guess != n_random:
            print("GameOver\nYou lose!!!")
            break
        guess = int(input("Outro número:    "))
        print(f"O número inteiro digitado foi: {guess}")
        turn += 1


def menu():
    print_opening_message('menu')
    choice = int(input("Which game do you wanna play?\nDigite o número: "))
    if choice == 1:
        guessing()
    elif choice == 2:
        hangman()
    else:
        print("ERROR!! Invalid Option!!!")


menu()

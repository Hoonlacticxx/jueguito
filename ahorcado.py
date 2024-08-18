import random

def choose_word(wordlist):
    word = random.choice(wordlist).upper()  
    return word

def show_status(hidden_word, used_letters):
    print("Adivina esta palabra:", end=" ")
    for letter in hidden_word:
        print(letter, end=" ")
    print("\nLetras usadas:", used_letters)

def play():
    with open('palabras.txt', 'r', encoding='utf-8') as f:
        words = f.read().splitlines()
    secret_word = choose_word(words)
    hidden_word = ["_"] * len(secret_word)
    used_letters = []
    attempts = 6
    
    print("Tienes", attempts, "intentos cariño")

    while attempts > 0:
        show_status(hidden_word, used_letters)
        letter = input("Elige una letra mi amor: ").upper()
        
        if letter in used_letters:
            print("Ya usaste esa letra cielo")
        elif letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    hidden_word[i] = letter
                    print("Te quedan", attempts, "intentos cielo")
        else:
            attempts -= 1
            print("Esa letra no está cariño")
            used_letters.append(letter)
            print("Te quedan", attempts, "intentos cielo")
            
        if "_" not in hidden_word:
            print("Yupiii, ganaste y adivinaste la palabra:", secret_word)
            break

    if "_" in hidden_word:
        print("Perdiste cielo :(. La palabra era:", secret_word)

play()
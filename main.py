import random
import re
import os
from unicodedata import normalize
import ahorcado_dolls

letters_used = []


def text_cleaner():
    unclean_text = open('./files/words.txt').read()
    clean_text = re.sub('[^A-Za-zÀ-ú0-9\s]+', '', unclean_text)
    open('./files/words.txt', 'w').write(clean_text)


def strip_accents_and_ñ(word):
    word = re.sub(
           r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
           normalize('NFD', word), 0, re.I
           )

    return normalize('NFC', word)


def charge_words_and_random():
    with open('./files/words.txt', 'r', encoding='unicode_escape') as f:
        words = [word.strip() for word in f]
        return random.choice(words)


def spawn_game(word):
    letters_from_word_list = []
    letters_from_word_list[:0] = word

    anonimous_letters_list = list(map(looker_for_word, letters_from_word_list))
    print(*anonimous_letters_list, '\n')

    return anonimous_letters_list


def game_loop(displays_per_level, failed_tries, target_word):

    while True:
        os.system('cls')
        print(displays_per_level[failed_tries])
        print('                               ', 'Letras: ', *letters_used, '\n')
        list_game = spawn_game(target_word)
        letter = strip_accents_and_ñ(
            input('Por favor, introduce una letra \n'
                  'introduce la palabra finalizar para resolver \n'
                  ' o introduce salir para terminar el juego: ').lower())

        if letter == 'finalizar':
            resolve(target_word)
            break
        if letter == 'salir':
            break
        if str.isdigit(letter):
            assert on_error_loop('Por favor, introduce una letra y no un número: ')
        elif len(letter) > 1:
            assert on_error_loop('Por favor, introduce únicamente una letra: ')
        elif letter in letters_used:
            failed_tries += 1
            pass
        elif letter not in target_word:
            failed_tries += 1
            letters_used.append(letter)
        else:
            letters_used.append(letter)

        if not'_' in list_game:
            print('Enhorabuena has ganado')
            break
        elif failed_tries == len(displays_per_level):
            print('Lo siento, has perdido, la palabra era {}'.format(target_word))
            break


def looker_for_word(letter_target):
    if strip_accents_and_ñ(letter_target.lower()) in letters_used:
        return letter_target
    elif letter_target == ' ':
        return ' '
    else:
        return '_'


def on_error_loop(phrase):
    while True:
        letter = input(phrase).lower()
        if str.isdigit(letter) & len(letter) == 1:
            return letter


def on_error_level(level):
    pass


def resolve(target_word):
    os.system('cls')
    spawn_game(target_word)

    word = strip_accents_and_ñ(input('Por favor, introduce la palabra para resolver: ').lower())
    target_word = strip_accents_and_ñ(target_word.lower())

    if word == target_word:
        print('Enhorabuena has ganado')
        return
    else:
        print('Lo siento, has perdido, la palabra era {}'.format(target_word))
        return


def main():
    text_cleaner()

    os.system('cls')
    print(ahorcado_dolls.ahorcado_title)

    another_game = True
    while another_game:
        failed_tries = 0
        target_word = charge_words_and_random()

        level = int(input('Bienvenido al Ahorcado, por favor, selecciona el nivel del 1 al 3: '))
        displays_per_level = ahorcado_dolls.ahorcado_display(level)
        game_loop(displays_per_level, failed_tries, target_word)

        another = input('¿Deseas continuar? y/n')
        if another.lower() != 'y':
            another_game = False


if __name__ == '__main__':
    main()
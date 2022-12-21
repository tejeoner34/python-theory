# Métodos

# string = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
# print(string.lstrip(",:%_#"))

# my_list = [1, 2, 15, 7, 2]
#
#
# def reduce_list(original_list):
#     return list(set(original_list))[0:-1]
#
#
# print(reduce_list(my_list))

# AHORCADO

from random import choice

words_list = ['test', 'otros']
chosen_word = choice(words_list)
lives = 6
lost_lives = 0
result_list = ['-'] * len(chosen_word)


def is_game_over():
    return lives == lost_lives


def letter_included(letter):
    return letter in chosen_word


def update_result_list(result_list, word, input_letter):
    for index, letter in enumerate(word):
        if letter == input_letter:
            result_list[index] = input_letter

    return result_list


while not is_game_over():
    print('number of lives:', lives - lost_lives)
    print(result_list)
    input_letter = input('Enter a letter: ')

    if letter_included(input_letter):
        result_list = update_result_list(result_list, chosen_word, input_letter)
        if('-' not in result_list):
            print('You won')
            break
    else:
        lost_lives += 1

print('Game over')





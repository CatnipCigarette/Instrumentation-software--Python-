function = input('Введите два слова:')
first_word = function [:function.find(' ')]
second_word = function [function.find(' ') + 1:]
print(second_word + ' ' + first_word)

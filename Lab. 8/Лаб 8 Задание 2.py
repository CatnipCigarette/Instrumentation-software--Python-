from collections import Counter
words_in_text = []

print('Введите текст:') 
for i in range(9):
    words_in_text.extend(input().split())
 
word_counter = Counter(words_in_text)
couples = [(-word[1], word[0]) for word in word_counter.most_common()]
words_in_text = [word[1] for word in sorted(couples)]

print('\n'.join(words_in_text))

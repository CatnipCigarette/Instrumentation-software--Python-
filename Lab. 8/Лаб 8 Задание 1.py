lines_of_text = int(input('Введите кол-во строк текста:'))
counter = {}
text = []

print('Введите текст:')
for i in range(lines_of_text):
    text = input().split()

for word in text:
    counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
frequent_word = [k for k, v in counter.items() if v == max_count]
print(min(frequent_word))

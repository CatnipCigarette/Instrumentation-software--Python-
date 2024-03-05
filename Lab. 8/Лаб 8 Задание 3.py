print('Введите хеш-теги:')
hashtags = dict()
line = input().split()
count = 0

for word in line:
    hashtags[word.lower()] = hashtags.get(word.lower(), 0) + 1
    count += 1
    
for tag in hashtags:
    if '#' not in tag:
        print('В хеш-теге не указан символ "#"!')
    if tag == '#':
        print('Хеш-тег состоит только из "#"!')    
    if hashtags[tag] > 1:
        print('Хеш-тег повторяется!')
    if count > 5:
        print('Указано больше 5 хеш-тегов!')
    if len(tag) > 20:
        print('Хеш-тег содержит больше 20 элементов!')
    if tag.count('#') > 1:
        print('Нет пробела между хеш-тегами!')


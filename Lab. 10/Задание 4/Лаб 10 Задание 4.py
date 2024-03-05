lines = 0
words = 0
letters = 0

for line in open('text.txt', 'r'):
    lines += 1
    letters += len(line)
    pos = 'out'
 
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
        
print('Input file contains:')
print(letters, 'letters')
print(words, 'words')
print(lines, 'lines')

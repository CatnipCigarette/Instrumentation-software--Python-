print('Введите строку с буквами h:')
line_with_h = input()
line_with_h = line_with_h[:line_with_h.find('h')] + line_with_h[line_with_h.rfind('h') + 1:]
print(line_with_h)

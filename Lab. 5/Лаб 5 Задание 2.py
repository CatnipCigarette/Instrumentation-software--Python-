list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_range=0
second_range=0
third_range=0

for i in list:
    if i >= 1 and i <= 3:
        first_range += 1
    if i >= 4 and i <= 6:
        second_range += 1
    if i >= 7 and i <= 9:
        third_range += 1
        
print('от 1 до 3: ', first_range)
print('от 4 до 6: ', second_range)
print('от 7 до 9: ', third_range)

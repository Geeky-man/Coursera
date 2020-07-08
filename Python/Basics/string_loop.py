fruit = 'banana'
'''index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index + 1

for letter in fruit:
    print(letter)
'''
counting = 0
for letter in fruit:
    if letter == '':
        counting = counting + 1
        print(counting)

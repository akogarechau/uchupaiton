from string import ascii_letters

user_string = input()
popular_letters = []

for character in ascii_letters:
   popular_letters.append(user_string.count(character))

max1 = popular_letters.index(max(popular_letters))
print('№1', ascii_letters[max1], popular_letters[max1])
popular_letters.pop(max1)

max2 = popular_letters.index(max(popular_letters))
print('№2', ascii_letters[max2], popular_letters[max2])
popular_letters.pop(max2)

max3 = popular_letters.index(max(popular_letters))
print('№3', ascii_letters[max3], popular_letters[max3])
popular_letters.pop(max3)




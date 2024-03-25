a_1 = 'a b c d e'
a_2 = 'a b c d e'

print(a_1 == a_2)
print(a_1 is a_2)

print('-' * 50)

b_1 = [1, 2, 3, 4]
b_2 = [1, 2, 3, 4]

print(b_1 == b_2)
print(b_1 is b_2)

print('-' * 50)

c_1 = '1 2 3 4 5 6'
c_2 = '1 2 3 4 5 6'

c_1 = tuple(c_1)
c_2 = tuple(c_2)

print(c_1 == c_2)
print(c_1 is c_2)

print('-' * 50)

word = "Hello"
word_2 = "Hello"

word = str(word)
word_2 = str(word_2)

print(word == word_2)
print(word is word_2)





# trans_table = str.maketrans('Maggie', '123456')
# print(trans_table)

# result = 'MaggieMaggie'.translate(trans_table)
# print(result)

# def greet(hello = 'hi'):
#     print('hello') 

#     greet(hello()) # hello
# print(greet) 

words = ['sky', 'apple', 'menu', 'atlas', 'books']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


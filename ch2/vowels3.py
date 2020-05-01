vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:  # 중복된 철자는 found 리스트에 저장 X
            found.append(letter)

for vowel in found:
    print(vowel)
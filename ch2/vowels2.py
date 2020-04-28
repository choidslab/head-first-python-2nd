vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
found = []

for letter in word:
    if letter in vowels:
        if letter not in found: # 중복된 철자는 found 리스트에 저장 X
            found.append(letter)

for vowel in found:
    print(vowel)

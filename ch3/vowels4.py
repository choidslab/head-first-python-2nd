
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

# Initialize Key
for key in vowels:
    found[key] = 0

# print(found)

for letter in word:
    if letter in vowels:
        # if letter not in found:  # 중복된 철자는 found 리스트에 저장 X
        #     found.append(letter)
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s).')

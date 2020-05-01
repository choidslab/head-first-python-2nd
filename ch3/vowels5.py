
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)  # 해당 dict에 key값이 존재하지 않을 경우 초기화, 그렇지 않을 경우 아무것도 하지 않음
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s).')

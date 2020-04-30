phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# Todo

# 내 풀이
new_phrase = phrase[1:3] + phrase[5:3:-1] + phrase[7:5:-1]

# 책 풀이
# new_phrase = ''.join(plist[1:3])
# new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)

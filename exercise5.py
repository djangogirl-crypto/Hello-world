wrd= input('enter a string')
wrd =str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print('palindrome')
else:
    print('no')
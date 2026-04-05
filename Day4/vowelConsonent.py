name = 'Programming'
vowels = ['a','e','i','o','u']
cons = 0
vowel = 0
for i in name:
    if i in vowels:
        vowel += 1
    else:
        cons += 1
print("vowels:",vowel)
print("consonent:",cons)
import itertools
letters = 'ВИШНЯ'
glas = 'ИЯ'
k = 0  
for i in itertools.product(letters, repeat=6):
    word = ''.join(i)  
    if word.count('В') <= 1 and word[0] != 'Ш' and word[-1] not in glas:
        k += 1
print(k)
from itertools import product
q = "ИЙКНОСТЧЫ"
t = "ТОКСИЧНЫЙ"
for i, word in enumerate(product(q, repeat=9), start=5):
    if ''.join(word) == t:
        print(i)
        break
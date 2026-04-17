qwe = '0123456789ABCDEFGHIJ'
qwe = qwe[::-1]
for x in qwe:
    n = int(f'912{x}8745', 21) + int(f'791{x}065', 21)
    if n % 20 == 0:
        print(n // 20)
        break
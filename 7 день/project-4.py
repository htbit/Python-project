alpha = ' abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ'
print ('ВНИМАНИЕ: программа работает только на английском языке')
v = int(input('1)Зашифровать.\n2)Расшифровать.\n'))
n = int(input('Сдвиг: '))
s = input().strip()
res = ''
if v == 1:
    for c in s:
        res += alpha[(alpha.index(c) + n) % len(alpha)]
elif v == 2:
    for c in s:
        res += alpha[(alpha.index(c) - n) % len(alpha)]
else:
    pass
print('Result: "' + res + '"')
print("1)Конвертер температур. \n2)Конвертер валют. \n3)Конвертер масс.")
a = float(input())
if a == 1:
    print("1)Из цельсия в фаренгейт. \n2)Из фаренгейт в цельсия.")
    b = float(input())
    if b == 1:
        t = float(input("°C: "))
        t = round(t)
        t = (t * (9/5) + 32)
        t = round(t, 1)
        print(str(t) + 'F')
    elif b == 2:
        t = float(input("°F: "))
        t = round(t)
        t = ((t - 32) * (5/9))
        t = round(t, 1)
        print(str(t) + '°C')
    else:
        exit
elif a == 2:
    print("1)Из Тенге в Рубли. \n2)Из Рублей в Тенге.")
    b = float(input())
    if b == 1:
        t = float(input("Тенге: "))
        t = round(t)
        t = (t * 0.17)
        t = round(t, -1)
        print('Рублей' + ' ' + str(t))
    elif b == 2:
        t = float(input("Рублей: "))
        t = round(t)
        t = (t / 0.17)
        t = round(t, -1)
        print('Тенге' + ' ' + str(t))
    else:
        exit
elif a == 3:
    print("1)Из килограмм в грамм. \n2)Из грамм в килограмм.")
    b = float(input())
    if b == 1:
        t = float(input("Килограмм: "))
        t = (t * 1000)
        print(str(t) + ' ' + 'грамм')
    elif b == 2:
        t = float(input("Грамм: "))
        t = (t / 1000)
        print(str(t) + ' ' + 'килограмм')
    else:
        exit
else:
    exit
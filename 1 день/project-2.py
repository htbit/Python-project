from collections import Counter
# подключине счетчика

def isPrime(x):
    # Проверяем, является ли данное число x простым или нет

    if x == 2:
        return True

    if x % 2 == 0:   
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True


def getExponent(n):
    # Подсчитывает одни и те же элементы в списке n возвращает список с показателем степени множественных элементов

    c = Counter(n)
    f = []

    for i in range(min(n), max(n) + 1):
        if i in n:
            if c[i] != 1:
                f.append(str(i) + '^' + str(c[i]))
            else:
                f.append(str(i))

    return f


def main():  # Функция-оболочка

    n = int(input('Введите число, чтобы найти его простые множители: '))

    f = []
    counter = 2

    while True:

        if n == 0 or n == 1:
            break

        for i in range(counter, n + 1):
            if n % i == 0:
                if isPrime(i):
                    f.append(i)
                    n //= i
                    break

    if len(f) != 0:
        f = getExponent(f)
        print(' * '.join(f))
    else:
        print('Число', n, 'не имеет никаких простых факторов.')

if __name__ == '__main__':
    main()
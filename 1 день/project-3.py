def isPrime(x):
    # Проверяем, является ли данное число x простым или нет

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False

    return True


def genPrime(currentPrime):
    # Возвращает следующий Prime после currentPrime

    newPrime = currentPrime + 1

    while True:

        if not isPrime(newPrime):
            newPrime += 1
        else:
            break

    return newPrime


def main():  # Функция-оболочка

    currentPrime = 2

    while True:

        answer = input('Не хотите ли вы посмотреть на следующую простое число? (Да/Нет) ')

        if answer.lower().startswith('д' or 'да' or 'y' or 'yes'):
            print(currentPrime)
            currentPrime = genPrime(currentPrime)

        else:
            break

if __name__ == '__main__':
    main()
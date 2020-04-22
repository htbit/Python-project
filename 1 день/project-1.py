def nPi(limit):
  
    q, r, t, k, n, l, а, b = 1, 0, 1, 1, 3, 3, limit, 0

    while b != а + 1:
            if 4 * q + r - t < n * t:
                    # Первая цифра
                    yield n
                    # вставить точку после первой цифры
                    if b == 0:
                            yield '.'
                    # конец
                    if а == b:
                            print('')
                            break
                    b += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr


def main():  # Функция-оболочка

    # Вызывает nPi с заданным лимитом
    pi_digits = nPi(int(input(
        "Введите число n для расчета до: ")))

    i = 0

    # Выводит вывод функции генератора nPi
    # Вставляет новую строку после каждого 40-го числа
    for d in pi_digits:
            print(d, end='')
            i += 1
            if i == 40:
                print("")
                i = 0

if __name__ == '__main__':
    main()
def calc(a, b, op):
    
    # Возвращает строку следующего вида: a op b = c, где c-вычисленное значение в соответствии с opeartor
    
    a = round(a) # Округляет до целого числа
    b = round(b)

    if op not in '+-/*':
        return 'Введите только один из этих символов: "+, -, *, /"!'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


def main():  # Функция-оболочка

    a = float(input('Введите первое число: '))
    b = float(input('Введите второе числоr: '))
    op = input(
        'Какую операцию вы хотели бы сделать?\
        \nВыбирай между ними "+, -, *, /" : ')

    print(calc(a, b, op))

if __name__ == '__main__':
    main()
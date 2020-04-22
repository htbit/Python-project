def palindrome(data):
    data = data.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'

str = input('Введите слово или предложение: ')
print(palindrome(str))
from string import punctuation
from random import randint
from re import findall
 
cryptMode = input("[З]ашифровать|[Р]асшифровать|Ручной ввод [К]люча: ").upper()
if cryptMode not in ['З','Р','К']:
    print("Ошибка: такой функции нет!"); input('Нажмите "ENTER" для выхода'); raise SystemExit
 
 
startMessage = input("Введите предложение для начала шифровки/расшифровки: ").upper() 
 
def clean(text):
    if not isinstance(text, str):
        raise TypeError('text должен быть str')
    return ''.join(x for x in text if x.isalpha() or x == "")
 
print("Отбрасываем все символы и пробелы из предложения: ", clean(startMessage))
xex = len(clean(startMessage))
print("В введённом предложении,", xex, "символов в тексте без пунктуации и пробелов.")
startMessage = clean(startMessage)
 
def regular(text):
    template = r"[0-9]+"
    return findall(template, text)
 
    
def encryptDecrypt(mode, message, final = "", keys = ""):
    if mode == 'З':
        for symbol in message:
            key = randint(0,32); keys += str(key) + "/"
            final += chr((ord(symbol) + key - 17)%33 + ord('А'))
        return final, keys
    elif mode == 'Р': 
        keys = input("Введите ключ: ")
        for index, symbol in enumerate(message):
            final += chr((ord(symbol) - int(regular(keys)[index]) - 17)%33 + ord('А'))
        return final
    else: 
        keys = input("Введите ключ: ")
        for index, symbol in enumerate(message):
            final += chr((ord(symbol) + int(regular(keys)[index]) - 17)%33 + ord('А'))
        return final
print("Финальное сообщение:",encryptDecrypt(cryptMode, startMessage))
input('Нажмите "ENTER" для выхода')
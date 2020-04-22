def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOUёуеыаоэяиюЁУЕЫАОЭЯИЮ")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    print("Всего было использовано гласных:", count)
str = input('Введите слово или предложение: ')
vowel_count(str)
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

proizv = int(input('Введите произведение чисел: '))
summa = int(input('Введите сумму чисел: '))
for x in range(1, 1001):
    if proizv % x == 0:
        y = proizv // x
        if y + x == summa:
            print(f'Петя загадал {x} и {y}')
            break
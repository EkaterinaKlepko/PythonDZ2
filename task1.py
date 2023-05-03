# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количетсво монеток: '))
count_orel = 0
count_reshka = 0
for i in range(n):
    position = input(f'Как лежит монетка №{i + 1}? ')
    if position == 'orel':
        count_orel += 1
    elif position == 'reshka':
        count_reshka += 1
if count_orel > count_reshka:
    print(f'Нужно перевернуть {count_reshka}')
else:
    print(f'нужно перевернуть {count_orel}')

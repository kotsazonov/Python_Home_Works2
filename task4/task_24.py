# Задача 24: В фермерском хозяйстве в Карелии выращивают
# чернику. Она растёт на круглой грядке, причём кусты
# высажены только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени
# сбора на них выросло различное число ягод — на i-ом
# кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора
# черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого
# куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым

# кустом заданной во входном файле грядки. ывр

# кустом заданной во входном файле грядки.


def max_berries(berries):
    n = len(berries)
    max_berries = 0
    for i in range(n):
        collected_berries = berries[i] + berries[i-1] + berries[(i+1) % n]
        max_berries = max(max_berries, collected_berries)
    return max_berries


n = int(input("Введите количество кустов на грядке: "))

berries = []
for i in range(n):
    berry_count = int(input("Введите количество ягод на кусте {}: ".format(i+1)))
    berries.append(berry_count)

# вызов функции для нахождения максимального количества ягод
result = max_berries(berries)

print("Максимальное количество ягод, которое можно собрать за один заход: ", result)

#Задача 32: Определить индексы элементов массива (списка),
#значения которых принадлежат заданному
#диапазону (т.е. не меньше заданного минимума и не больше
#заданного максимума)
def find_indices_in_range(lst, min_val, max_val):
    """
    Возвращает индексы элементов списка, значения которых принадлежат заданному диапазону.
    lst: список значений
    min_val: минимальное значение диапазона
    max_val: максимальное значение диапазона
    """
    return [index for index, value in enumerate(lst) if min_val <= value <= max_val]

def main():
    # Ввод данных
    n = int(input("Введите количество элементов в списке: "))
    values = [float(input(f"Введите значение элемента {i + 1}: ")) for i in range(n)]
    min_val = float(input("Введите минимальное значение диапазона: "))
    max_val = float(input("Введите максимальное значение диапазона: "))

    # Нахождение индексов и вывод результатов
    indices = find_indices_in_range(values, min_val, max_val)
    print(f"Индексы элементов, принадлежащих диапазону от {min_val} до {max_val}:")
    print(indices)

if __name__ == "__main__":
    main()
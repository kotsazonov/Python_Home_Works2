import os


def load_directory(file_name="directory.txt"):
    """Загружает телефонный справочник из файла."""
    if not os.path.exists(file_name):
        return []

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    directory = []
    for line in lines:
        surname, name, patronymic, phone_number = line.strip().split(';')
        directory.append({
            "surname": surname,
            "name": name,
            "patronymic": patronymic,
            "phone_number": phone_number
        })
    return directory


def save_directory(directory, file_name="directory.txt"):
    """Сохраняет телефонный справочник в файл."""
    with open(file_name, "w", encoding="utf-8") as file:
        for entry in directory:
            file.write(f'{entry["surname"]};{entry["name"]};{entry["patronymic"]};{entry["phone_number"]}\n')


def search_entry(directory, keyword):
    """Ищет запись в справочнике по ключевому слову."""
    results = [entry for entry in directory if
               keyword.lower() in entry["name"].lower() or keyword.lower() in entry["surname"].lower()]
    return results


def update_entry(directory, old_entry, new_entry):
    """Обновляет запись в справочнике."""
    index = directory.index(old_entry)
    directory[index] = new_entry


def delete_entry(directory, entry):
    """Удаляет запись из справочника."""
    directory.remove(entry)


def display_directory(directory):
    """Выводит телефонный справочник."""
    for entry in directory:
        print(f'{entry["surname"]} {entry["name"]} {entry["patronymic"]} - {entry["phone_number"]}')


def main():
    directory = load_directory()

    while True:
        print("\nВыберите действие:")
        print("1. Показать справочник")
        print("2. Добавить запись")
        print("3. Поиск и редактирование записей")
        print("4. Сохранить справочник")
        print("5. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            display_directory(directory)
        elif choice == "2":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            directory.append({
                "surname": surname,
                "name": name,
                "patronymic": patronymic,
                "phone_number": phone_number
            })
        elif choice == "3":
            keyword = input("Введите имя или фамилию для поиска: ")
            results = search_entry(directory, keyword)
            display_directory(results)

            if results:
                action = input("Выберите действие (изменить/удалить/ничего): ")
                if action == "изменить":
                    old_entry = results[0]
                    print("Введите новые данные:")
                    surname = input("Введите фамилию: ")
                    name = input("Введите имя: ")
                    patronymic = input("Введите отчество: ")
                    phone_number = input("Введите номер телефона: ")
                    new_entry = {
                        "surname": surname,
                        "name": name,
                        "patronymic": patronymic,
                        "phone_number": phone_number
                    }
                    update_entry(directory, old_entry, new_entry)
                    print("Запись обновлена.")
                elif action == "удалить":
                    delete_entry(directory, results[0])
                    print("Запись удалена.")
        elif choice == "4":
            save_directory(directory)
            print("Справочник сохранен.")
        elif choice == "5":
            print("До свидания!")
            break


if __name__ == "__main__":
    main()
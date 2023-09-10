def count_vowels(phrase):
    """Считает количество гласных букв в фразе."""
    vowels = 'аеёиоуыэюя'
    return sum(1 for char in phrase if char in vowels)


def check_rhythm(poem):
    # Разделяем стихотворение на фразы
    phrases = poem.split()

    # Получаем количество гласных в первой фразе
    vowel_count = count_vowels(phrases[0])

    # Проверяем каждую фразу на соответствие количеству гласных
    for phrase in phrases:
        if count_vowels(phrase) != vowel_count:
            return False

    return True


if __name__ == "__main__":
    poem_input = input("Введите стихотворение: ").strip()

    if check_rhythm(poem_input):
        print("Парам пам-пам")
    else:
        print("Пам парам")


# Функція для форматування тексту
def format_text(text):
    # Перетворення всіх літер на малі
    text = text.lower()
    # Видалення пунктуації та пробілів
    text = text.translate(text.maketrans('', '', '.-:,;?!()'))
    text = text.rstrip()
    return text


if __name__ == '__main__':
    # Введення користувачем тексту для обробки
    user_text = input('Введіть текст: ')
    # Форматування тексту
    formatted_text = format_text(user_text)
    # Виведення відформатованого тексту
    print('Відформатований текст: ', formatted_text)
    # Введення користувачем слова або словосполучення для заміни
    word_to_replace = input('Яке слово або словосполучення дажаєте замінити? ')
    # Пошук індексу замінюваного слова/словосполучення у відформатованому тексті
    index = formatted_text.find(word_to_replace)
    # Виведення індексу замінюваного слова/словосполучення
    print(f'Словосполучення "{word_to_replace}" знаходиться на індексі {index}.')
    # Введення користувачем нового слова для заміни
    new_word = input('На яке слово бажаєте замінити? ')
    # Заміна слова/словосполучення на нове слово
    edited_text = formatted_text.replace(word_to_replace, new_word)
    # Виведення відредагованого тексту
    print('Відредагований текст: ', edited_text)

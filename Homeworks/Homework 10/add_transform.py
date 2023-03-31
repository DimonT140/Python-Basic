import os


def save_notes(notes: list[str], file_path: str) -> None:
    """
    Функція отримує список рядків та шлях до файлу, відкриває файл у режимі запису ('w') та записує
    кожен рядок окремо на новому рядку у файлі.

    :param notes: список рядків, які потрібно записати у файл
    :param file_path: шлях до файлу, у який потрібно записати нотатки
    :return: None
    """
    with open(file_path, 'w') as f:  # відкриваємо файл у режимі запису ('w')
        # записуємо кожен елемент списку notes окремо у новому рядку у файлі
        f.write('\n'.join(notes))


def load_notes(file_path: str) -> list[str]:
    """
    Функція завантажує нотатки з файлу за заданим шляхом.

    :param file_path: шлях до файлу нотаток.
    :return: список нотаток або пустий список.
    """
    # перевіряємо наявність файлу за заданим шляхом
    if os.path.exists(file_path):
        # відкриваємо файл і читаємо його вміст
        with open(file_path, 'r') as f:
            # для кожного рядка з файлу видаляємо символ переносу рядка ('\n') та додаємо до списку
            return [line.rstrip('\n') for line in f.readlines()]
    else:
        # якщо файл не знайдено, повертаємо пустий список
        return []


def print_notes(notes: list[str]) -> None:
    """
    Функція виводить список нотаток.
    Якщо список порожній, то виводиться повідомлення про відсутність записів.
    В іншому випадку, виводиться пронумерований список нотаток.

    :param notes: Список нотаток.
    :return: None
    """
    # перевіряємо чи список порожній.
    if not notes:
        print("Немає записів." '\n')
    else:
        # виводимо повідомлення про наявність записів.
        print("Записи:")
        # проходимось по кожній нотатці та  виводимо її на екран.
        for i, note in enumerate(notes):
            print(f"{i+1}. {note}")
        print()


def add_note(notes: list[str]) -> None:
    """
    Функція додає новий запис у список notes.

    :return: None
    """
    note: str = input("Введіть запис: ")  # отримуємо від користувача новий запис
    notes.append(note)  # додаємо його до списку notes
    print()


def transform_note(notes: list[str]) -> None:
    """
    Функція трансформує запис у списку.
    :return: None
    """
    # виводимо список записів
    print_notes(notes)
    # просим вибрати номер запису для трансформації
    choice = input("Введіть номер запису для трансформації: ")
    try:
        choice = int(choice)
        # перевіряємо, чи введений номер є дійсним
        if choice == 0 or choice > len(notes):
            print("Неправильний номер." '\n')
        else:
            # вибір запису за номером
            note = notes[choice-1]
            # знаходимо літеру 'a', видаляємо все до неї та робимо першу літеру великою
            # якщо літеру 'a' не знайдено, то повертаємо порожній рядок
            # заміняємо вибраний запис трансформованим
            notes[choice-1] = note[note.find('a'):].strip('\n').capitalize() if 'a' in note else ''
            # виводим запис до та після трансформації
            print(f"Трансформовано запис: {note} -> {notes[choice-1]}" '\n')
    # запобігаєм "зламу" програми від невірного вводу користувача
    except (ValueError, IndexError):
        # виводим повідомлення користувачу після невірного вводу
        print("Неправильний номер." '\n')

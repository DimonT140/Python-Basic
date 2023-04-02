notes = []  # список для зберігання нотаток
num_of_notes = 0  # лічильник кількості нотаток


def add_note() -> None:
    """
    Додає нову нотатку до списку notes і збільшує лічильник num_of_notes на 1.
    :return: None
    """
    global num_of_notes  # використовуємо глобальну змінну для збільшення лічильника
    note = input("Введіть вашу нотатку: ")  # запит на введення нотатки
    notes.append(note)  # додаємо нотатку до списку
    num_of_notes += 1  # збільшуємо лічильник на 1
    print()  # друк пустого рядка для красоти :)


def print_notes(notes_to_print: list) -> None:
    """
    Виводить на екран всі нотатки зі списку notes_to_print.
    :param notes_to_print: список нотаток, які потрібно вивести на екран
    :return: None
    """
    for note in notes_to_print:
        print(note)  # друк кожної нотатки


def earliest_notes() -> None:
    """
    Виводить на екран перші num_notes найраніших нотаток зі списку notes.
    :return: None
    """
    global num_of_notes  # використовуємо глобальну змінну для перевірки кількості нотаток
    num_notes = int(input("Скільки найраніших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = [note for i, note in sorted(enumerate(notes))]  # сортуємо за порядком додавання
    print_notes(sorted_notes[:num_notes])  # виведення найраніших нотаток
    print()  # друк пустого рядка


def latest_notes() -> None:
    """
    Виводить на екран перші num_notes найпізніших нотаток зі списку notes.
    :return: None
    """
    global num_of_notes  # використовуємо глобальну змінну для перевірки кількості нотаток
    num_notes = int(input("Скільки найпізніших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = [note for i, note in sorted(enumerate(notes), reverse=True)]  # сортуємо за зворотнім порядком додавання
    print_notes(sorted_notes[:num_notes])  # виведення найпізніших нотаток
    print()  # друк пустого рядка


def longest_notes() -> None:
    """
    Функція, що виводить найдовші нотатки зі списку заміток.
    :return: None
    """
    global num_of_notes  # глобальна змінна
    num_notes = int(input("Скільки найдовших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = sorted(notes, key=len, reverse=True)  # сортування нотаток за довжиною в порядку спадання
    print_notes(sorted_notes[:num_notes])  # виведення найдовших нотаток
    print()  # друк пустого рядка


def shortest_notes() -> None:
    """
    Функція, що виводить найменші нотатки зі списку заміток.
    :return: None
    """
    global num_of_notes  # глобальна змінна
    num_notes = int(input("Скільки найкоротших нотаток вивести? "))  # запит на введення кількості найкоротших нотаток
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = sorted(notes, key=len)  # сортування нотаток за довжиною в порядку зростання
    print_notes(sorted_notes[:num_notes])  # виведення найкоротших нотаток
    print()  # друк пустого рядка

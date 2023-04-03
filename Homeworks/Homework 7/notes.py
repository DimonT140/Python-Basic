notes = []


def add_note() -> str:
    """
    Зчитує нотатку та повертає її
    :return: нотатка
    """
    note = input("Введіть вашу нотатку: ")  # запит на введення нотатки
    notes.append(note)  # додаємо нотатку до списку
    num_of_notes = len(notes)  # отримуємо кількість нотаток у списку
    num_of_notes += 1  # збільшуємо лічильник на 1
    print()  # друк пустого рядка для красоти :)
    return note


def print_notes(notes_to_print: list):
    """
    Виводить на екран всі нотатки зі списку notes_to_print.
    :param notes_to_print: список нотаток, які потрібно вивести на екран
    """
    for note in notes_to_print:
        print(note)  # друк кожної нотатки


def earliest_notes(notes: list):
    """
    Виводить на екран перші num_notes найраніших нотаток зі списку notes_to_print.
    :param notes: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(notes)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найраніших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = [note for i, note in sorted(enumerate(notes))]  # сортуємо за порядком додавання
    print_notes(sorted_notes[:num_notes])  # виведення найраніших нотаток
    print()  # друк пустого рядка


def latest_notes(notes: list):
    """
    Виводить на екран перші num_notes найпізніших нотаток зі списку notes.
    :param notes: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(notes)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найпізніших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = [note for i, note in sorted(enumerate(notes), reverse=True)]  # сортуємо за зворотнім порядком додавання
    print_notes(sorted_notes[:num_notes])  # виведення найпізніших нотаток
    print()  # друк пустого рядка


def longest_notes(notes: list):
    """
    Функція, що виводить найдовші нотатки зі списку заміток.
    :param notes: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(notes)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найдовших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = sorted(notes, key=len, reverse=True)  # сортування нотаток за довжиною в порядку спадання
    print_notes(sorted_notes[:num_notes])  # виведення найдовших нотаток
    print()  # друк пустого рядка


def shortest_notes(notes: list):
    """
    Функція, що виводить найкоротші нотатки зі списку заміток.
    :param notes: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(notes)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найкоротших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = sorted(notes, key=len)  # сортування нотаток за довжиною в порядку зростання
    print_notes(sorted_notes[:num_notes])  # виведення найкоротших нотаток
    print()  # друк пустого рядка

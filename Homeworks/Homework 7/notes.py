def add_note(list_of_notes: list) -> list:
    """
    Зчитує нотатку та повертає її
    :return: нотатка
    """
    note = input("Введіть вашу нотатку: ")  # запит на введення нотатки
    list_of_notes.append(note)  # додаємо нотатку до списку
    print()  # друк пустого рядка для красоти :)
    return list_of_notes


def print_notes(notes_to_print: list):
    """
    Виводить на екран всі нотатки зі списку notes_to_print.
    :param notes_to_print: список нотаток, які потрібно вивести на екран
    """
    for note in notes_to_print:
        print(note)  # друк кожної нотатки


def earliest_notes(note_list: list):
    """
    Виводить на екран перші num_notes найраніших нотаток зі списку notes_to_print.
    :param note_list: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(note_list)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найраніших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    # виведення найраніших нотаток, тобто безпосередньо самого списку
    print_notes(note_list[:num_notes])
    print()  # друк пустого рядка


def latest_notes(note_list: list):
    """
    Виводить на екран перші num_notes найпізніших нотаток зі списку notes.
    :param note_list: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(note_list)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найпізніших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    # виведення найраніших нотаток, тобто безпосередньо самого оберненого списку
    print_notes(note_list[::-1][:num_notes])
    print()  # друк пустого рядка


def longest_notes(note_list: list):
    """
    Функція, що виводить найдовші нотатки зі списку заміток.
    :param note_list: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(note_list)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найдовших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = sorted(note_list, key=len, reverse=True)  # сортування нотаток за довжиною в порядку спадання
    print_notes(sorted_notes[:num_notes])  # виведення найдовших нотаток
    print()  # друк пустого рядка


def shortest_notes(note_list: list):
    """
    Функція, що виводить найкоротші нотатки зі списку заміток.
    :param note_list: список нотаток, які потрібно підготувати для виводу на екран
    """
    num_of_notes = len(note_list)  # змінна для перевірки кількості нотаток
    num_notes = int(input("Скільки найкоротших нотаток вивести? "))
    if num_notes > num_of_notes:
        print(f"Не більше {num_of_notes} \n")  # повідомлення, що не можна вивести більше, ніж є наявних нотаток
        return
    sorted_notes = sorted(note_list, key=len)  # сортування нотаток за довжиною в порядку зростання
    print_notes(sorted_notes[:num_notes])  # виведення найкоротших нотаток
    print()  # друк пустого рядка

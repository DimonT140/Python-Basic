import time

# словник для зберігання нотаток
notes = {}


def add_note():
    """Додає нову нотатку в словник"""
    note_text = input("Введіть текст нотатки: ")
    timestamp = time.time()
    notes[timestamp] = note_text
    print("Нотатка успішно додана!")


def print_notes(sort_order, limit=None):
    """Виводить нотатки в залежності від способу сортування та обмеження кількості"""
    sorted_notes = sorted(notes.items(), reverse=sort_order)
    if limit:
        sorted_notes = sorted_notes[:limit]
    for _, note_text in sorted_notes:
        print(note_text)


if __name__ == '__main__':
    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest, exit): ")
        if command == "add":
            add_note()
        elif command == "earliest":
            print_notes(sort_order=False)
        elif command == "latest":
            print_notes(sort_order=True)
        elif command == "longest":
            limit = int(input("Скільки найбільших нотаток вивести? "))
            print_notes(sort_order=True, limit=limit)
        elif command == "shortest":
            limit = int(input("Скільки найменших нотаток вивести? "))
            print_notes(sort_order=False, limit=limit)
        elif command == "exit":
            break
        else:
            print("Неправильна команда, спробуйте ще раз.")

"""
this is note
this is notissimo
note
this is a huge long, insanely long note
well, anyways

add
earliest
latest
longest
shortest
exit
"""

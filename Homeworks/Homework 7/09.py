

notes = []


def add_note():
    note = input("Введіть текст нотатки: ")
    notes.append(note)
    print("Нотатка додана.")


def print_notes(reverse=False, by_length=False, limit=None):
    if by_length:
        notes_sorted = sorted(notes, key=len, reverse=reverse)
    else:
        notes_sorted = sorted(notes, reverse=reverse)
    if limit is not None:
        notes_sorted = notes_sorted[:limit]
    for note in notes_sorted:
        print(note)


if __name__ == '__main__':
    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest, exit): ")
        if command == 'add':
            add_note()
        elif command == 'earliest':
            limit = int(input("Скільки нотаток вивести? "))
            print("Нотатки (найраніші - найпізніші):")
            print_notes(reverse=False, limit=limit)
        elif command == 'latest':
            limit = int(input("Скільки нотаток вивести? "))
            print("Нотатки (найпізніші - найраніші):")
            print_notes(reverse=True, limit=limit)
        elif command == 'longest':
            limit = int(input("Скільки нотаток вивести? "))
            print("Найбільші нотатки:")
            print_notes(by_length=True, reverse=True, limit=limit)
        elif command == 'shortest':
            limit = int(input("Скільки нотаток вивести? "))
            print("Найменші нотатки:")
            print_notes(by_length=True, limit=limit)
        elif command == 'exit':
            print("До побачення!")
            break
        else:
            print("Невідома команда.")
'''
Введіть нотатку: this is note
Введіть нотатку: this is notissimo
Введіть нотатку: note
Введіть нотатку: this is a huge long, insanely long note
Введіть нотатку: well, anyways
add
earliest
latest
longest
shortest
exit
'''

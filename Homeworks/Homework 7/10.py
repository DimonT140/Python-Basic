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
            try:
                limit = int(input("Скільки нотаток вивести? "))
                print("Нотатки (найраніші - найпізніші):")
                print_notes(reverse=False, limit=limit)
            except ValueError:
                print("Некоректний ввід. Введіть ціле число.")
        elif command == 'latest':
            try:
                limit = int(input("Скільки нотаток вивести? "))
                print("Нотатки (найпізніші - найраніші):")
                print_notes(reverse=True, limit=limit)
            except ValueError:
                print("Некоректний ввід. Введіть ціле число.")
        elif command == 'longest':
            try:
                limit = int(input("Скільки нотаток вивести? "))
                print("Найбільші нотатки:")
                print_notes(by_length=True, reverse=True, limit=limit)
            except ValueError:
                print("Некоректний ввід. Введіть ціле число.")
        elif command == 'shortest':
            try:
                limit = int(input("Скільки нотаток вивести? "))
                print("Найменші нотатки:")
                print_notes(by_length=True, limit=limit)
            except ValueError:
                print("Некоректний ввід. Введіть ціле число.")
        elif command == 'exit':
            print("До побачення!")
            break
        else:
            print("Невідома команда.")

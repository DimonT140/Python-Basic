notes = []


def add_note():
    note = input("Введіть текст нотатки: ")
    notes.append(note)


def show_notes(sort_key=None, reverse=False, limit=None):
    if sort_key is None:
        sort_key = lambda x: None

    sorted_notes = sorted(notes, key=sort_key, reverse=reverse)

    if limit is not None:
        sorted_notes = sorted_notes[:limit]

    for i, note in enumerate(sorted_notes):
        print(f"{i + 1}. {note}")


if __name__ == '__main__':
    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest, exit): ")

        if command == "add":
            add_note()
        elif command == "earliest":
            count = int(input("Скільки нотаток відобразити? "))
            show_notes(sort_key=lambda x: notes.index(x), limit=count)
        elif command == "latest":
            count = int(input("Скільки нотаток відобразити? "))
            show_notes(sort_key=lambda x: notes.index(x), reverse=True, limit=count)
        elif command == "longest":
            count = int(input("Скільки нотаток відобразити? "))
            show_notes(sort_key=lambda x: len(x), reverse=True, limit=count)
        elif command == "shortest":
            count = int(input("Скільки нотаток відобразити? "))
            show_notes(sort_key=lambda x: len(x), limit=count)
        elif command == "exit":
            break
        else:
            print("Невідома команда")

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

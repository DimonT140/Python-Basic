notes = []

def add_note():
    note = input("Введіть текст нотатки: ")
    notes.append(note)
    print("Нотатка додана.")

def print_notes(reverse=False, by_length=False):
    if by_length:
        notes_sorted = sorted(notes, key=len, reverse=reverse)
    else:
        notes_sorted = sorted(notes, reverse=reverse)
    for note in notes_sorted:
        print(note)

if __name__ == '__main__':
    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest, exit): ")
        if command == 'add':
            add_note()
        elif command == 'earliest':
            print("Нотатки (найраніші - найпізніші):")
            print_notes()
        elif command == 'latest':
            print("Нотатки (найпізніші - найраніші):")
            print_notes(reverse=True)
        elif command == 'longest':
            print("Нотатки (від найдовшої до найкоротшої):")
            print_notes(by_length=True, reverse=True)
        elif command == 'shortest':
            print("Нотатки (від найкоротшої до найдовшої):")
            print_notes(by_length=True)
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


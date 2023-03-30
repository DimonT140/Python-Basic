notes = []

def add_note():
    note = input("Введіть текст нотатки: ")
    notes.append((len(notes), note))
    print("Нотатка додана.")

def print_notes(reverse=False):
    if reverse:
        notes_sorted = sorted(notes, reverse=True)
    else:
        notes_sorted = sorted(notes)
    for note in notes_sorted:
        print(note[0], note[1])

if __name__ == '__main__':
    while True:
        command = input("Введіть команду (add, earliest, latest, exit): ")
        if command == 'add':
            add_note()
        elif command == 'earliest':
            print("Нотатки (найраніші - найпізніші):")
            print_notes()
        elif command == 'latest':
            print("Нотатки (найпізніші - найраніші):")
            print_notes(reverse=True)
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

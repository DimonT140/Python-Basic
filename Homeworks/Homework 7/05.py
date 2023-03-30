def add_note():
    note = input("Введіть нотатку: ")
    notes.append(note)

def show_notes(sort_func, limit=None):
    sorted_notes = sort_func(notes)
    if limit is not None:
        sorted_notes = sorted_notes[:limit]
    for note in sorted_notes:
        print(note)

def sort_by_length(notes):
    return sorted(notes, key=len)

def sort_by_time(notes):
    return notes.copy()

def reverse_sort(sort_func):
    return lambda notes: list(reversed(sort_func(notes)))

notes = []

COMMANDS = {
    'add': add_note,
    'earliest': lambda: show_notes(sort_by_time, int(input("Скільки нотаток відобразити? "))),
    'latest': lambda: show_notes(reverse_sort(sort_by_time), int(input("Скільки нотаток відобразити? "))),
    'longest': lambda: show_notes(reverse_sort(sort_by_length), int(input("Скільки нотаток відобразити? "))),
    'shortest': lambda: show_notes(sort_by_length, int(input("Скільки нотаток відобразити? ")))
}

if __name__ == '__main__':
    while True:
        command = input("Введіть команду: ")
        if command in COMMANDS:
            COMMANDS[command]()
        elif command == 'exit':
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

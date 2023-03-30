from notes import add_note, show_notes, sort_by_length, sort_by_time, reverse_sort
notes = []

COMMANDS = {
    'add': add_note,
    'earliest': lambda: show_notes(sort_by_time),
    'latest': lambda: show_notes(reverse_sort(sort_by_time)),
    'longest': lambda: show_notes(sort_by_length),
    'shortest': lambda: show_notes(reverse_sort(sort_by_length))
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
'''

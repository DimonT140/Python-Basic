def add_note(notes=None):
    note = input("Введіть нотатку: ")
    notes.append(note)


def sort_by_length(notes, reverse_order):
    return sorted(notes, key=len, reverse=reverse_order)


def sort_by_time(notes, reverse_order):
    return notes[::-1] if reverse_order else notes


def print_notes(notes=None):
    print("Список нотаток:")
    for note in notes:
        print(note)

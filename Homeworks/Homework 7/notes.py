def add_note(notes=None):
    note = input("Введіть нотатку: ")
    notes.append(note)


def show_notes(sort_func, limit=None, notes=None):
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

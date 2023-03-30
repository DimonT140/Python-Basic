notes = []
timestamps = []


def add_note():
    note = input("Введіть вашу нотатку: ")
    notes.append(note)
    timestamps.append(time.time())


def print_notes(notes_to_print):
    for note in notes_to_print:
        print(note)


def get_timestamp(note_index):
    return timestamps[note_index]


def earliest_notes():
    num_notes = int(input("Введіть кількість нотаток для відображення: "))
    sorted_indices = sorted(range(len(notes)), key=get_timestamp)
    sorted_notes = [notes[i] for i in sorted_indices]
    print_notes(sorted_notes[:num_notes])


def latest_notes():
    num_notes = int(input("Введіть кількість нотаток для відображення: "))
    sorted_indices = sorted(range(len(notes)), key=get_timestamp, reverse=True)
    sorted_notes = [notes[i] for i in sorted_indices]
    print_notes(sorted_notes[:num_notes])


def longest_notes():
    num_notes = int(input("Введіть кількість нотаток для відображення: "))
    sorted_notes = sorted(notes, key=len, reverse=True)
    print_notes(sorted_notes[:num_notes])


def shortest_notes():
    num_notes = int(input("Введіть кількість нотаток для відображення: "))
    sorted_notes = sorted(notes, key=len)
    print_notes(sorted_notes[:num_notes])


if __name__ == '__main__':
    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest): ")
        if command == 'add':
            add_note()
        elif command == 'earliest':
            earliest_notes()
        elif command == 'latest':
            latest_notes()
        elif command == 'longest':
            longest_notes()
        elif command == 'shortest':
            shortest_notes()
        else:
            print("Неправильна команда")


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

notes = []

def add_note():
    note = input("Введіть вашу нотатку: ")
    notes.append(note)

def print_notes(notes_to_print):
    for note in notes_to_print:
        print(note)

def earliest_notes():
    num_notes = int(input("Введіть кількість нотаток для відображення: "))
    sorted_notes = sorted(notes, reverse=False)
    print_notes(sorted_notes[:num_notes])

def latest_notes():
    num_notes = int(input("Введіть кількість нотаток для відображення: "))
    sorted_notes = sorted(notes, reverse=True)
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

'''


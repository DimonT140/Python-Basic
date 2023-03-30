import time

# Функція додавання нотатки
def add_note():
    note = input("Введіть текст нотатки: ")
    timestamp = time.time()  # Отримання поточного часу в секундах
    notes.append((timestamp, note))
    print("Нотатку додано")

# Функція виведення нотаток
def print_notes(notes_list):
    for note in notes_list:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(note[0])), note[1])

# Функція виведення найранішої або найпізнішої нотатки
def print_earliest_or_latest_notes(notes_list, reverse=False):
    notes_list.sort(reverse=reverse)
    num_notes = input("Скільки нотаток ви бажаєте побачити? ")
    num_notes = int(num_notes)
    print_notes(notes_list[:num_notes])

# Список для зберігання нотаток
notes = []

if __name__ == '__main__':
    while True:
        print("Введіть команду: add, earliest, latest або exit")
        command = input().strip().lower()

        if command == "add":
            add_note()
        elif command == "earliest":
            print_earliest_or_latest_notes(notes_list=notes)
        elif command == "latest":
            print_earliest_or_latest_notes(notes_list=notes, reverse=True)
        elif command == "exit":
            break
        else:
            print("Невідома команда")

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

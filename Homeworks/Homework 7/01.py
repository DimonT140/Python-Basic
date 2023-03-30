from notes2 import add_note, sort_by_length, sort_by_time

if __name__ == '__main__':
    notes = []
    while True:
        command = input("Введіть одну з команд (add/earliest/latest/longest/shortest/exit): ")
        if command == "add":
            add_note()
        elif command == "earliest":
            print("Від найранішої до найпізнішої:")
            for note in sort_by_time(notes, False):
                print(note)
        elif command == "latest":
            print("Від найпізнішої до найранішої:")
            for note in sort_by_time(notes, True):
                print(note)
        elif command == "longest":
            print("Від найдовшої до найкоротшої:")
            for note in sort_by_length(notes, True):
                print(note)
        elif command == "shortest":
            print("Від найкоротшої до найдовшої:")
            for note in sort_by_length(notes, False):
                print(note)
        elif command == "exit":
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")


'''
Введіть нотатку: this is note
Введіть нотатку: this is notissimo
Введіть нотатку: note
Введіть нотатку: this is a huge long, insanely long note
Введіть нотатку: well, anyways
'''

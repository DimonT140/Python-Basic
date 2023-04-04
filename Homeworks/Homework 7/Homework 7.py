from notes import add_note, earliest_notes, latest_notes, longest_notes, shortest_notes

if __name__ == '__main__':
    my_notes = []
    while True:  # нескінченний цикл буде продовжуватись, доки не буде введена команда "exit"
        command = input("Введіть команду (add, earliest, latest, longest, shortest, exit): ")  # просимо користувача ввести команду
        if command == 'add':  # якщо команда "add", викликаємо функцію add_note(my_notes)
            add_note(my_notes)
        elif command == 'earliest':  # якщо команда "earliest", викликаємо функцію earliest_notes(my_notes)
            earliest_notes(my_notes)
        elif command == 'latest':  # якщо команда "latest", викликаємо функцію latest_notes(my_notes)
            latest_notes(my_notes)
        elif command == 'longest':  # якщо команда "longest", викликаємо функцію longest_notes(my_notes)
            longest_notes(my_notes)
        elif command == 'shortest':  # якщо команда "shortest", викликаємо функцію shortest_notes(my_notes)
            shortest_notes(my_notes)
        elif command == "exit":  # якщо команда "exit", виходимо з циклу
            break
        else:  # якщо команда не відповідає жодній з визначених, виводимо повідомлення про помилку
            print("Неправильна команда!" '\n')

from notes import add_note, earliest_notes, latest_notes, longest_notes, shortest_notes

if __name__ == '__main__':
    while True:  # нескінченний цикл буде продовжуватись, доки не буде введена команда "exit"
        command = input("Введіть команду (add, earliest, latest, longest, shortest, exit): ")  # просимо користувача ввести команду
        if command == 'add':  # якщо команда "add", викликаємо функцію add_note()
            add_note()
        elif command == 'earliest':  # якщо команда "earliest", викликаємо функцію earliest_notes()
            earliest_notes()
        elif command == 'latest':  # якщо команда "latest", викликаємо функцію latest_notes()
            latest_notes()
        elif command == 'longest':  # якщо команда "longest", викликаємо функцію longest_notes()
            longest_notes()
        elif command == 'shortest':  # якщо команда "shortest", викликаємо функцію shortest_notes()
            shortest_notes()
        elif command == "exit":  # якщо команда "exit", виходимо з циклу
            break
        else:  # якщо команда не відповідає жодній з визначених, виводимо повідомлення про помилку
            print("Неправильна команда!" '\n')

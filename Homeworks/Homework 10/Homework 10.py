from add_transform import save_notes, load_notes, print_notes, add_note, transform_note

if __name__ == '__main__':
    # запускаєм програму, завантажуєм нотатки з вказаного файлу та виводим на екран
    notes_file = input("Введіть шлях до файлу для завантаження нотаток: ")
    notes = load_notes(notes_file)
    print_notes(notes)
    while True:
        # запитуємо про дію у користувача
        action = input("Введіть дію (додати, трансформувати, зберегти, вийти): ")
        # оброблюємо вибрану дію
        if action == "додати":
            add_note(notes)
        elif action == "трансформувати":
            transform_note(notes)
        elif action == "зберегти":
            # питаєм куди зберегти та зберігаєм нотатки
            save_file = input("Введіть шлях до файлу для збереження нотаток: ")
            # якщо користувач не ввів шлях для збереження, то зберігаєм в notes.txt
            if not save_file:
                save_file = "notes.txt"
                save_notes(notes, save_file)
            print(f"Збережено у файл {save_file}" '\n')
        elif action == "вийти":
            # зберігаємо зміни
            if notes_file.strip() != "":
                save_notes(notes, notes_file)
            # виходимо з програми
            print("Вихід з програми.")
            break
        else:
            # виводим повідомлення користувачу після невірного вводу
            print("Неправильна дія." '\n')

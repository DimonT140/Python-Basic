from transformer import transform_lines


if __name__ == '__main__':
    file_path = 'notes.txt'
    while True:
        transformed_lines = transform_lines(file_path)
        # Виводимо список рядків на екран
        print(transformed_lines)
        choice = input("Вийти? (так/ні) ")
        if choice.lower() == 'так':
            break

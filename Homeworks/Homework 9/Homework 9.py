from transformer import transform_lines


if __name__ == '__main__':
    file_path = 'notes.txt'
    transformed_lines = transform_lines(file_path)
    # Виводимо список рядків на екран
    print(transformed_lines)

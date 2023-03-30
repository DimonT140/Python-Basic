def transform_lines(file_path):
    # Відкриваємо файл для читання
    with open(file_path, 'r') as f:
        # Отримуємо всі рядки з файлу та видаляємо символи нового рядка
        lines = [line.rstrip('\n') for line in f.readlines()]
        # знаходимо підрядок 'a', видаляємо все до нього та робимо першу літеру великою
        # якщо підрядок 'a' не знайдено, то повертаємо порожній рядок
        transformed_lines = [line[line.find('a'):].strip().capitalize() if 'a' in line else '' for line in lines]
        return transformed_lines

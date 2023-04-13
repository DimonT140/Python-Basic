import csv  # імпортуємо модуль csv
from items import count_items, get_items, show_brand_distribution

if __name__ == '__main__':
    file_path = 'tech_inventory.csv'  # Шлях до файлу
    data = []  # Список для зберігання даних
    with open(file_path, 'r') as file:  # Відкриття файлу на читання
        reader = csv.DictReader(file)  # Створюємо читача csv-файлу
        for row in reader:  # Прохід по рядках файлу
            data.append(row)  # Додавання рядку до списку даних
    count_items(data, 'brand')  # Виклик функції count_items для брендів
    count_items(data, 'category')  # Виклик функції count_items для категорій
    get_items(data, 'brand')  # Виклик функції get_items для брендів
    get_items(data, 'category')  # Виклик функції get_items для категорій
    show_brand_distribution(data)  # Виклик функції show_brand_distribution для розподілу брендів

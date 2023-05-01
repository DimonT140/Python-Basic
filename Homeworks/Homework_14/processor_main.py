from FileProcessor import CSVFileProcessor, JSONFileProcessor  # імпортуємо класи для обробки csv та json файлів
import os  # імпортуємо модуль для роботи з операційною системою
import tkinter as tk  # імпортуємо модуль для створення графічного інтерфейсу користувача
from PIL import Image, ImageTk  # імпортуємо модуль для роботи з зображеннями

if __name__ == '__main__':
    # Створюємо об'єкти класів CSV та JSON для обробки даних.
    processor = [
        JSONFileProcessor(processor_filenames=[], data=[], sku_index={}, warehouse_index={}, operation_index={}),
        CSVFileProcessor(processor_filenames=[], data=[], sku_index={}, warehouse_index={}, operation_index={})
    ]  # Список процесорів.
    for p in processor:  # Перебираємо усі процесори в списку.
        # Перевіряємо, чи існує список процесорів та його довжина більше 0.
        if p.processor_filenames and len(p.processor_filenames) > 0:
            # Перевіряємо чи існує файл з назвою, яка міститься в списку процесорів.
            if os.path.isfile(p.processor_filenames[0]):
                p.data = p.load_file(p.processor_filenames[0])  # Завантажуємо дані з файлу в процесор.
            else:  # Якщо файл не знайдено,
                print(f"Файл {p.processor_filenames[0]} не знайдено.")  # виводимо повідомлення про помилку.
        else:  # Якщо список процесорів порожній,
            print("Список файлів порожній")  # виводимо повідомлення про помилку.
        # Створюємо індекси SKU, складу та операцій для процесору
        p.sku_index, p.warehouse_index, p.operation_index = p.create_indices(p.data)
        # Розраховуємо метрики
        sale_profit, sku_expired, warehouse_count, warehouse_sold, warehouse_disposed = p.calculate_metric_x()
        if p.processor_filenames:  # Якщо назва файлу визначена для поточного процесору,
            print(f"Оброблено файл: {p.processor_filenames[0]}")  # виводимо повідомлення про обробку файлу.
        else:  # Якщо назва файлу не визначена для поточного процесору,
            print("Файли не оброблено.")  # виводимо повідомлення.
        # Виведимо результати
        print(f"Прибуток від продажу: ${sale_profit:.2f}")
        print(f"Кількість просрочених SKU: {sku_expired}")
        print("Кількості товарів на кожному складі:")
        for i, (warehouse, count) in enumerate(warehouse_count.items()):  # виведимо кількість товарів на кожному складу
            print(f"Склад {warehouse}: {count} товарів")
            if (i + 1) % 10 == 0:  # якщо кількість складів більше 10, то виводимо питання користувачу
                input("Натисніть Enter для продовження")
        print("Кількість проданих товарів на кожному складі:")  # виведимо кількість проданих товарів на кожному складу
        for i, (warehouse, count) in enumerate(warehouse_sold.items()):
            print(f"Склад {warehouse}: {count} проданих товарів")
            if (i + 1) % 10 == 0:  # якщо кількість складів більше 10, то виводимо питання користувачу
                input("Натисніть Enter для продовження")
        print(
            "Кількість утилізованих товарів на кожному складі:")  # виведимо кількість утилізованих товарів на кожному складу
        for i, (warehouse, count) in enumerate(warehouse_disposed.items()):
            print(f"Склад {warehouse}: {count} утилізованих товарів")
            if (i + 1) % 10 == 0:  # якщо кількість складів більше 10, то виводимо питання користувачу
                input("Натисніть Enter для продовження")
        print(f"Прибуток від продажу: ${sale_profit:.2f}")
        print(f"Кількість просрочених SKU: {sku_expired}")
        print("Кількості товарів на кожному складі:")
        for warehouse, count in warehouse_count.items():  # Кількості товарів на кожному складі.
            print(f"Склад {warehouse}: {count} товарів")
        print("Кількість проданих товарів на кожному складі:")
        for warehouse, count in warehouse_sold.items():  # Кількість проданих товарів на кожному складі.
            print(f"Склад {warehouse}: {count} проданих товарів")
        print("Кількість утилізованих товарів на кожному складі:")
        for warehouse, count in warehouse_disposed.items():
            print(
                f"Склад {warehouse}: {count} утилізованих товарів")  # Кількість утилізованих товарів на кожному складі.
    # Відкриття файлу з діаграмою.
    image_path = 'FileProcessor(UML_class).png'  # Отримуємо шлях до файлу
    root = tk.Tk()  # Створюємо вікно Tkinter
    root.title("FileProcessor")
    image = Image.open(image_path)  # Відкриваємо зображення за допомогою PIL
    tk_image = ImageTk.PhotoImage(image)  # Конвертуємо зображення у формат, зрозумілий для Tkinter
    label = tk.Label(root, image=tk_image)  # Створюємо елемент Label і відображаємо на ньому зображення
    label.pack()
    root.mainloop()  # Запускаємо головний цикл Tkinter, який чекає подій

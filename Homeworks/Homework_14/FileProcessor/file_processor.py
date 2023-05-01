import csv  # імпортуємо модуль для роботи з csv файлами
import datetime  # імпортуємо модуль для роботи з датою та часом
import json  # імпортуємо модуль для роботи з json форматом
from typing import List, Dict, Tuple  # імпортуємо типи даних, які будуть використані в коді


class DataEntry:
    """
    Представляє запис даних про одну операцію з продажу та зберігання товарів на складі.
    """

    def __init__(self, date: datetime.date, time: datetime.time, sku: str, warehouse: str, warehouse_cell_id: int,
                 operation: str, invoice: int, expiration_date: datetime.date, operation_cost: float,
                 comment: str) -> None:
        """
        Ініціалізує об'єкт DataEntry із заданими параметрами.
        :param date: дата операції
        :param time: час операції
        :param sku: унікальний ІД товару над яким виконуються операції
        :param warehouse: унікальний ІД складу де відбувається операції
        :param warehouse_cell_id: номер полиці на складі, де знаходиться цей товар
        :param operation: тип операції
        :param invoice: номер інвойсу (пересилання)
        :param expiration_date: дата закінчення терміну придатності товару
        :param operation_cost: ціна операції (менше ноля якщо витрати, більше якщо прибуток)
        :param comment: коментар до операції
        """
        # ініціалізуємо всі властивості класу DataEntry
        self.date = date  # дата операції
        self.time = time  # час операції
        self.sku = sku  # унікальний ІД товару
        self.warehouse = warehouse  # унікальний ІД складу
        self.warehouse_cell_id = warehouse_cell_id  # номер полиці на складі
        self.operation = operation  # тип операції
        self.invoice = invoice  # номер інвойсу
        self.expiration_date = expiration_date  # дата закінчення терміну придатності товару
        self.operation_cost = operation_cost  # ціна операції
        self.comment = comment  # коментар до операції

    def __str__(self) -> str:
        """
        Метод класу DataEntry
        :return: рядок зі значеннями всіх властивостей об'єкту
        """
        return f"Date: {self.date}\nTime: {self.time}\nSKU: {self.sku}\nWarehouse: {self.warehouse}\nWarehouse Cell ID: " \
               f"{self.warehouse_cell_id}\nOperation: {self.operation}\nInvoice: {self.invoice}\nExpiration Date: " \
               f"{self.expiration_date}\nOperation Cost: {self.operation_cost}\nComment: {self.comment}"


class FileProcessor:
    """
    Клас для обробки файлів та збереження даних у відповідні індекси.
    """

    def __init__(self, processor_filenames: List[str], data: List[DataEntry], sku_index: Dict[str, List[DataEntry]],
                 warehouse_index: Dict[str, List[DataEntry]], operation_index: Dict[str, List[DataEntry]]) -> None:
        """
        Ініціалізує об'єкт із заданими параметрами.
        :param processor_filenames: список імен файлів, які будуть оброблені
        :param data: список екземплярів класу DataEntry, які будуть збережені
        :param sku_index: індекс, який зберігає екземпляри класу DataEntry за стовпчиком sku
        :param warehouse_index: індекс, який зберігає екземпляри класу DataEntry за стовпчиком warehouse
        :param operation_index: індекс, який зберігає екземпляри класу DataEntry за стовпчиком operation
        """
        # Ініціалізуємо атрибути класу
        self.processor_filenames = processor_filenames  # список імен файлів
        self.data = data  # список екземплярів класу DataEntry
        self.sku_index = sku_index  # індекс за стовпчиком sku
        self.warehouse_index = warehouse_index  # індекс за стовпчиком warehouse
        self.operation_index = operation_index  # індекс за стовпчиком operation

    def __str__(self) -> str:
        """
        Метод класу FileProcessor.
        :return: рядок із інформацією про об'єкт класу FileProcessor.
        """
        return f"FileProcessor(processor_filenames={self.processor_filenames}, data={self.data}, sku_index={self.sku_index}, " \
               f"warehouse_index={self.warehouse_index}, operation_index={self.operation_index})"

    @staticmethod  # декоратор, який дозволяє визначити статичний метод
    def load_file(filename: str) -> List[DataEntry]:
        """
        Завантажує дані з файлу, перевіряє його розширення та на основі цього виконує операції з
        файлом. Якщо розширення файлу є `json`, то відбувається завантаження json-даних з файлу та їх обробка з
        використанням створення екземплярів класу `DataEntry`. Якщо розширення файлу є `csv`, то відбувається
        завантаження csv-даних з файлу та їх обробка з використанням створення екземплярів класу `DataEntry`.
        :param filename: назва файлу
        :return: список `data_entries`, що містить всі створені екземпляри класу `DataEntry`.
        """
        file_extension = filename.split(".")[-1]  # визначаємо формат файлу з переданого шляху до файлу
        data_entries = []  # створюємо порожній список, який буде заповнюватися об'єктами DataEntry.
        if file_extension == "json":  # перевіряємо, чи файл є json-файлом.
            with open(filename, "r") as f:  # відкриваємо файл з вказаним ім'ям в режимі читання.
                json_data = json.load(f)  # зчитуємо дані з json-файлу та зберігаємо їх у змінну json_data.
                for entry in json_data:  # проходимося по кожному елементу зі списку json_data.
                    # створюємо об'єкт DataEntry зі значеннями з json-файлу та зберігаємо його у змінну data_entry.
                    data_entry = DataEntry(**entry)
                    data_entries.append(data_entry)  # додаємо об'єкт data_entry до списку data_entries.
        elif file_extension == "csv":  # якщо формат файлу не є json, перевіряємо, чи файл є csv-файлом.
            with open(filename, "r") as f:  # відкриваємо файл з вказаним ім'ям в режимі читання.
                # створюємо об'єкт csv.DictReader для зчитування файлу у вигляді словника.
                csv_reader = csv.DictReader(f)
                for row in csv_reader:  # проходимося по кожному словнику в csv_reader.
                    # створюємо об'єкт DataEntry зі значеннями з csv-файлу та зберігаємо його у змінну data_entry
                    data_entry = DataEntry(**row)
                    data_entries.append(data_entry)  # додаємо об'єкт data_entry до списку data_entries.
        else:  # якщо формат файлу не підтримується,
            raise ValueError("Файл не підтримується.")  # видаємо помилку.
        return data_entries  # повертаємо список об'єктів DataEntry

    @staticmethod  # декоратор, який дозволяє визначити статичний метод
    def create_indices(data: List[DataEntry]) -> Tuple[Dict[str, List[DataEntry]], Dict[str, List[DataEntry]],
                                                       Dict[str, List[DataEntry]]]:
        """
        Створює індекси, які зберігають об'єкти DataEntry зі списку data за такими критеріями:
        * sku_index - індексує DataEntry за стовпчиком sku,
        * warehouse_index - індексує DataEntry за стовпчиком warehouse,
        * operation_index - індексує DataEntry за стовпчиком operation.
        :param data: Список DataEntry, які необхідно проіндексувати.
        :return: Кортеж із трьох словників, кожен із яких є індексом DataEntry за певним критерієм.
        """
        sku_index = {}  # словник для індексування за стовпчиком sku
        warehouse_index = {}  # словник для індексування за стовпчиком warehouse
        operation_index = {}  # словник для індексування за стовпчиком operation
        for row in data:  # проходимо по кожному рядку даних
            sku = row.sku  # отримуємо значення стовпчика sku
            warehouse = row.warehouse  # отримуємо значення стовпчика warehouse
            operation = row.operation  # отримуємо значення стовпчика operation
            if sku not in sku_index:  # якщо sku ще не міститься у словнику sku_index
                sku_index[sku] = [row]  # створюємо новий ключ та додаємо рядок даних до списку
            else:  # якщо sku вже є у словнику sku_index
                sku_index[sku].append(row)  # додаємо рядок даних до списку за відповідним ключем
            if warehouse not in warehouse_index:  # якщо warehouse ще не міститься у словнику warehouse_index
                warehouse_index[warehouse] = [row]  # створюємо новий ключ та додаємо рядок даних до списку
            else:  # якщо warehouse вже є у словнику warehouse_index
                warehouse_index[warehouse].append(row)  # додаємо рядок даних до списку за відповідним ключем
            if operation not in operation_index:  # якщо operation ще не міститься у словнику operation_index
                operation_index[operation] = [row]  # створюємо новий ключ та додаємо рядок даних до списку
            else:  # якщо operation вже є у словнику operation_index
                operation_index[operation].append(row)  # додаємо рядок даних до списку за відповідним ключем
        # повертаємо кортеж з трьома словниками, які містять індекси за різними критеріями
        return sku_index, warehouse_index, operation_index

    def calculate_metric_x(self) -> Tuple[float, int, Dict[str, int], Dict[str, int], Dict[str, int]]:
        """
        Розраховує метрики на основі даних про операції з продажу та зберігання товарів у складах.
        :return: кортеж, який містить наступні п'ять елементів:
                 * `sale_profit`: прибуток від усіх операцій типу sale (сума колонки operation_cost де колонка operation == 'sale'),
                 * `len(sku_expired)`: кількість унікальних SKU було втрачено (expiration_date минуло і sale не відбулося),
                 * `warehouse_count`: словник, який містить кількість товарів, що "пройшло" через кожний склад (warehouse),
                 * `warehouse_sold`: словник, який містить кількість товарів було продано з кожного складу (warehouse),
                 * `warehouse_disposed`: словник, який містить кількість товарів було утилізовано (dispose) з кожного складу (warehouse).
        """
        # Ініціалізуємо змінні для підрахунку метрик.
        sale_profit = 0  # збір загального прибутку від продажу.
        sku_expired = set()  # множина прострочених SKU.
        warehouse_count = {}  # словник кількості товарів в кожному складі.
        warehouse_sold = {}  # словник кількості проданих товарів з кожного складу.
        warehouse_disposed = {}  # словник кількості вибракованих товарів з кожного складу.
        # Обходимо список записів про події.
        for data_entry in self.data:  # проходимо по кожному запису в self.data.
            # Підраховуємо загальний прибуток від продажу.
            if data_entry.operation == 'sale':  # якщо операція - продаж,
                sale_profit += data_entry.operation_cost  # додаємо витрати на операцію до прибутку.
            # Підраховуємо прострочені SKU.
            # якщо дата придатності минула, і операція не продаж,
            if data_entry.expiration_date < data_entry.date and data_entry.operation != 'sale':
                sku_expired.add(data_entry.sku)  # додаємо SKU до множини прострочених.
            # Підраховуємо кількість товарів на складах.
            if data_entry.warehouse not in warehouse_count:  # якщо склад відсутній в словнику,
                warehouse_count[data_entry.warehouse] = 0  # додаємо склад до словника зі значенням 0,
            warehouse_count[data_entry.warehouse] += 1  # додаємо одиницю до кількості товарів на складі.
            # Підраховуємо кількість проданих товарів з кожного складу.
            if data_entry.operation == 'sale':  # якщо операція - продаж,
                if data_entry.warehouse not in warehouse_sold:  # якщо склад відсутній в словнику,
                    warehouse_sold[data_entry.warehouse] = 0  # додаємо склад до словника зі значенням 0,
                warehouse_sold[
                    data_entry.warehouse] += 1  # додаємо одиницю до кількості проданих товарів з цього складу.
            # Підраховуємо кількість вибракованих товарів з кожного складу.
            if data_entry.operation == 'dispose':  # якщо операція - вибраковка,
                if data_entry.warehouse not in warehouse_disposed:  # якщо склад відсутній в словнику,
                    warehouse_disposed[data_entry.warehouse] = 0  # додаємо склад до словника зі значенням 0,
                warehouse_disposed[
                    data_entry.warehouse] += 1  # додаємо одиницю до кількості вибракованих товарів з цього складу.
        # повертаємо загальний прибуток від продажу, кількість прострочених SKU, словник кількості товарів на
        # кожному складі, словник кількості проданих товарів з кожного складу та словник кількості вибракованих товарів з кожного складу.
        return sale_profit, len(sku_expired), warehouse_count, warehouse_sold, warehouse_disposed

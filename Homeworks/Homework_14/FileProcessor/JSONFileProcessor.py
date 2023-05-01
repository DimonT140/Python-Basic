from .file_processor import DataEntry, FileProcessor  # імпортуємо класи DataEntry і FileProcessor з модуля file_processor
import datetime  # імпортуємо модуль для роботи з датою та часом
import json  # імпортуємо модуль для роботи з json форматом
import os  # імпортуємо модуль для роботи з операційною системою
from typing import List, Dict  # імпортуємо типи даних, які будуть використані в коді


class JSONFileProcessor(FileProcessor):
    """
    Клас для обробки файлів у форматі JSON. Наслідує клас FileProcessor.
    """

    def __init__(self, processor_filenames: List[str], data: List[DataEntry], sku_index: Dict[str, List[DataEntry]],
                 warehouse_index: Dict[str, List[DataEntry]], operation_index: Dict[str, List[DataEntry]]) -> None:
        """
        ініціалізує об'єкт при створенні нового екземпляру класу.
        :param processor_filenames: список імен файлів, які будуть оброблені.
        :param data: список екземплярів класу DataEntry, які будуть збережені.
        :param sku_index: індекс, який зберігає екземпляри класу DataEntry за стовпчиком sku.
        :param warehouse_index: індекс, який зберігає екземпляри класу DataEntry за стовпчиком warehouse.
        :param operation_index: індекс, який зберігає екземпляри класу DataEntry за стовпчиком operation.
        """
        super().__init__(processor_filenames, data, sku_index, warehouse_index, operation_index)

    def __str__(self) -> str:
        """
        Метод класу JSONFileProcessor
        :return: Рядок із іменами оброблюваних файлів та кількістю записів у кожному індексі.
        """
        return f"JSONFileProcessor(processor_filenames={self.processor_filenames}, sku_index={len(self.sku_index)}, " \
               f"warehouse_index={len(self.warehouse_index)}, operation_index={len(self.operation_index)})"

    @staticmethod
    def load_file(filename: str) -> List[DataEntry]:
        """
        Завантажує файли JSON з інформацією про товарні партії та перетворює цю інформацію на список об'єктів DataEntry.
        :param filename: назва файлу, що містить інформацію про товарні партії.
        :return: список об'єктів DataEntry, який містить інформацію про товарні партії, що містяться у файлі JSON.
        """
        data_entries = []  # створюємо порожній список для зберігання даних
        with open(os.path.join('sku', filename)) as f:  # відкриваємо файл із заданим ім'ям
            json_data = json.load(f)  # зчитуємо дані з файлу у форматі JSON
            for item in json_data:  # перебираємо всі записи в файлі
                date = datetime.datetime.strptime(item['date'], '%d-%b-%Y').date()  # зчитуємо дату операції
                time = datetime.datetime.strptime(item['time'], '%H:%M:%S').time()  # зчитуємо час операції
                sku = item['sku']  # зчитуємо SKU товару
                warehouse = item['warehouse']  # зчитуємо склад, на якому проведена операція
                warehouse_cell_id = item['warehouse_cell_id']  # зчитуємо ідентифікатор полиці на складі
                operation = item['operation']  # зчитуємо тип операції
                invoice = item['invoice']  # зчитуємо номер накладної
                # зчитуємо дату закінчення терміну придатності товару
                expiration_date = datetime.datetime.strptime(item['expiration_date'], '%d-%b-%Y').date()
                operation_cost = item['operation_cost']  # зчитуємо вартість операції
                comment = item['comment']  # зчитуємо коментар до операції
                data_entry = DataEntry(date, time, sku, warehouse, warehouse_cell_id, operation, invoice,
                                       expiration_date,
                                       operation_cost, comment)  # створюємо об'єкт класу DataEntry зі зчитаними даними
                data_entries.append(data_entry)  # додаємо об'єкт класу DataEntry до списку даних
        return data_entries  # повертаємо список даних, зчитаних з файлу

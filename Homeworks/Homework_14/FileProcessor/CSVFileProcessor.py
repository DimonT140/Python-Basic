from .file_processor import DataEntry, FileProcessor  # імпортуємо класи DataEntry і FileProcessor з модуля file_processor
import csv  # імпортуємо модуль для роботи з csv файлами
import datetime  # імпортуємо модуль для роботи з датою та часом
import os  # імпортуємо модуль для роботи з операційною системою
from typing import List, Dict  # імпортуємо типи даних, які будуть використані в коді


class CSVFileProcessor(FileProcessor):
    """
    Клас для обробки файлів у форматі CSV. Наслідує клас FileProcessor.
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
        Метод класу CSVFileProcessor
        :return: Рядок із іменами оброблюваних файлів та кількістю записів у кожному індексі.
        """
        return f"CSVFileProcessor(processor_filenames={self.processor_filenames}, sku_index={len(self.sku_index)}, " \
               f"warehouse_index={len(self.warehouse_index)}, operation_index={len(self.operation_index)})"

    def load_file(filename: str) -> List[DataEntry]:
        """
        Завантажує файли CSV з інформацією про товарні партії та перетворює цю інформацію на список об'єктів DataEntry.
        :param filename: назва файлу, що містить інформацію про товарні партії.
        :return: список об'єктів DataEntry, який містить інформацію про товарні партії, що містяться у файлі CSV.
        """
        with open(os.path.join('sku', filename), 'r') as f:  # відкриваємо файл в режимі читання
            reader = csv.reader(f)  # створюємо об'єкт csv.reader для читання даних з файлу
            next(reader)  # переходимо до наступного рядка у файлі
            data_entries = []  # створюємо порожній список, в який будуть зберігатися DataEntry об'єкти
            for row in reader:  # цикл для ітерації по рядках у файлі
                date = datetime.datetime.strptime(row[0], '%d-%b-%Y').date()  # зчитуємо дату операції
                time = datetime.datetime.strptime(row[1], '%H:%M:%S').time()  # зчитуємо час операції
                sku = row[2]  # зчитуємо SKU товару
                warehouse = row[3]  # зчитуємо склад, на якому проведена операція
                warehouse_cell_id = int(row[4])  # перетворюємо рядок з номером полиці у ціле число
                operation = row[5]  # зчитуємо тип операції
                invoice = int(row[6])  # перетворюємо рядок з номером інвойсу у ціле число
                # зчитуємо дату закінчення терміну придатності товару
                expiration_date = datetime.datetime.strptime(row[7], '%d-%b-%Y').date()
                operation_cost = float(row[8])  # перетворення рядка з вартістю операції у десятичне число
                comment = row[9]  # зчитуємо коментар до операції
                data_entry = DataEntry(date, time, sku, warehouse, warehouse_cell_id, operation, invoice,
                                       expiration_date,
                                       operation_cost, comment)  # створюємо об'єкт класу DataEntry зі зчитаними даними
                data_entries.append(data_entry)  # додаємо об'єкт класу DataEntry до списку даних
        return data_entries  # повертаємо список даних, зчитаних з файлу

from .data_entry import DataEntry  # імпортуємо клас DataEntry з модуля data_entry
from .file_processor import FileProcessor  # імпортуємо клас FileProcessor з модуля file_processor
import csv  # імпортуємо модуль для роботи з csv файлами
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

    def load_file(self, filename: str):
        """
        Завантажує файли CSV з інформацією про товарні партії та перетворює цю інформацію на список об'єктів DataEntry.
        :param filename: назва файлу, що містить інформацію про товарні партії.
        :return: список об'єктів DataEntry, який містить інформацію про товарні партії, що містяться у файлі CSV.
        """
        with open(filename, 'r') as f:  # відкриваємо файл в режимі читання
            reader = csv.DictReader(f)  # створюємо об'єкт csv.reader для читання даних з файлу
            for row in reader:  # цикл для ітерації по рядках у файлі
                data_entry = DataEntry(**row)  # створюємо об'єкт класу DataEntry зі зчитаними даними
                self.data.append(data_entry)  # додаємо об'єкт класу DataEntry до списку даних

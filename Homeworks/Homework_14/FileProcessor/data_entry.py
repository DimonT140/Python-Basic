import datetime  # імпортуємо модуль для роботи з датою та часом


class DataEntry:
    """
    Представляє запис даних про одну операцію з продажу та зберігання товарів на складі.
    """

    def __init__(self, date: str, time: str, sku: str, warehouse: str, warehouse_cell_id: str,
                 operation: str, invoice: int, expiration_date: str, operation_cost: str,
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
        self.date = datetime.datetime.strptime(date, '%d-%b-%Y').date()  # зчитуємо дату операції
        self.time = datetime.datetime.strptime(time, '%H:%M:%S').time()  # час операції
        self.sku = sku  # унікальний ІД товару
        self.warehouse = warehouse  # унікальний ІД складу
        self.warehouse_cell_id = warehouse_cell_id  # номер полиці на складі
        self.operation = operation  # тип операції
        self.invoice = invoice  # номер інвойсу
        self.expiration_date = datetime.datetime.strptime(expiration_date, '%d-%b-%Y').date()  # дата закінчення терміну придатності товару
        self.operation_cost = float(operation_cost)  # ціна операції
        self.comment = comment  # коментар до операції

    def __str__(self) -> str:
        """
        Метод класу DataEntry
        :return: рядок зі значеннями всіх властивостей об'єкту
        """
        return f"Date: {self.date}\nTime: {self.time}\nSKU: {self.sku}\nWarehouse: {self.warehouse}\nWarehouse Cell ID: " \
               f"{self.warehouse_cell_id}\nOperation: {self.operation}\nInvoice: {self.invoice}\nExpiration Date: " \
               f"{self.expiration_date}\nOperation Cost: {self.operation_cost}\nComment: {self.comment}"


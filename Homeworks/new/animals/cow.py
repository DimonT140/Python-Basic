from .animal import Animal
from random import randint  # импортируем функцию randint из модуля random


class Cow(Animal):
    """
    Класс, описывающий объект "корова".
    """
    def __init__(self, name: str, preferred_food: set, age: int, treat_hours: int,
                 sleeping_hours: int, month: int) -> None:
        """
        Конструктор класса Cow.
        :param name: str - имя коровы.
        :param preferred_food: set - предпочитаемая еда коровы.
        :param age: int - возраст коровы.
        :param treat_hours: int - количество часов заботы о корове.
        :param sleeping_hours: int - количество часов сна курицы.
        :param month: int - количество месяцев с последнего визита к ветеринару.
        """
        super().__init__(name, preferred_food, age, treat_hours, sleeping_hours, month)
        self.say_word = "Му-у-у!"
        self.animal_type = "Корова"

    def treat(self, treat_hours: int = randint(0, 5)) -> str:
        """
        Метод заботиться о корове.
        :param treat_hours: Количество часов заботы о корове. По умолчанию - случайное число от 0 до 5.
        :return: Строка с наградой за заботу о корове (молоко).
        """
        if self.treat_hours == 0:
            print(f'{self.name} без заботы')
        else:
            print(f'Вы заботитесь о {self.name} {self.treat_hours} час(а)(ов)!')
        return "Молоко"

    def sleeping(self, hours: int = randint(0, 5)) -> None:
        """
        Метод для сна коровы.
        :param hours: Количество часов сна. По умолчанию - случайное число от 0 до 5.
        :return: Информация о сне.
        """
        # если корова не спит, то выводим сообщение об этом
        if self.sleeping_hours == 0:
            print(f'{self.name} не спит')
        else:
            # иначе выводим сообщение о количестве часов сна
            print(f'{self.name} спит {self.sleeping_hours} час(а)(ов)')

    def last_vet_visit(self, months: int = randint(0, 6)) -> None:
        """
        Метод, определяющий время последнего и следующего визита к ветеринару.
        :param months: Количество месяцев, прошедших с последнего визита к ветеринару.
                       По умолчанию - случайное число от 0 до 6.
        :return: Информация о посещении ветеринара.
        """
        print(f"С последнего визита к ветеринару прошло {months} мес., следующий, через {6 - months} мес.")
        if months == 6:
            print(f'{self.name} идет к ветеринару...')
        elif months == 0:
            print(f'{self.name} уже был(а) у ветеринара')

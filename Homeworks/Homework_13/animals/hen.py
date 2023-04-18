from .animal import Animal
from random import randint  # импортируем функцию randint из модуля random


class Hen(Animal):
    """
    Класс, описывающий объект "курица".
    """
    def __init__(self, name: str, preferred_food: set, age: int, treat_hours: int,
                 sleeping_hours: int, month: int) -> None:
        """
        Конструктор класса Hen.
        :param name: str - имя курицы.
        :param preferred_food: set - предпочитаемая еда курицы.
        :param age: int - возраст курицы.
        :param treat_hours: int - количество часов заботы о курице.
        :param sleeping_hours: int - количество часов сна курицы.
        :param month: int - количество месяцев с последнего визита к ветеринару.
        """
        super().__init__(name, preferred_food, age, treat_hours, sleeping_hours, month)
        self.say_word = "Кудах-кудах!"
        self.animal_type = "Курица"

    def treat(self, treat_hours: int = randint(0, 5)) -> str:
        """
        Метод заботиться о курице.
        :param treat_hours: Количество часов заботы о курице. По умолчанию - случайное число от 0 до 5.
        :return: Строка с наградой за заботу о курице (яйца).
        """
        if self.treat_hours == 0:  # Если о курице не заботились, то выводим сообщение об этом
            print(f'{self.name} без заботы')
        else:  # Иначе выводим сообщение о количестве часов заботы.
            print(f'Вы заботитесь о {self.name} {self.treat_hours} час(а)(ов)!')
        return "Куриные яйца."

from .animal import Animal
from random import randint  # импортируем функцию randint из модуля random


class Dog(Animal):
    """
    Класс, описывающий объект "собака".
    """
    def __init__(self, name: str, preferred_food: set, age: int, treat_hours: int,
                 sleeping_hours: int, month: int) -> None:
        """
        Конструктор класса Dog.
        :param name: str - имя собаки.
        :param preferred_food: set - предпочитаемая еда собаки.
        :param age: int - возраст собаки.
        :param treat_hours: int - продолжительность прогулки с собакой.
        :param sleeping_hours: int - продолжительность сна собаки.
        :param month: int - количество месяцев с последнего визита к ветеринару.
        """
        super().__init__(name, preferred_food, age, treat_hours, sleeping_hours, month)
        self.say_word = "Гав-гав!"
        self.animal_type = "Собака"

    def treat(self, hours: int = randint(0, 5)) -> str:
        """
        Метод гулять с собакой.
        :param hours: Количество часов прогулки. По умолчанию - случайное число от 0 до 5.
        :return: Сообщение о хорошем настроении.
        """
        if self.treat_hours == 0:  # Если собака не гуляет, то выводим сообщение об этом
            print(f'{self.name} не гуляет')
        elif self.treat_hours <= 3:  # Если прогулка была короткой, то выводим сообщение о том, что собака не нагулялялась
            print(f'{self.name} гуляет {self.treat_hours} час(а)(ов)! не нагулялся(ась) :(')
        elif self.treat_hours == 5:  # Если прогулка была продолжительной, то выводим сообщение о том, что собака устало
            print(f'{self.name} гуляет {self.treat_hours} час(а)(ов)! приятно устал(а) :)')
        else:    # Иначе выводим сообщение о количестве часов прогулки
            print(f'Вы гуляете с {self.name} {self.treat_hours} час(а)(ов)!')
            return "Хорошее настроение"

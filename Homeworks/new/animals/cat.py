from .animal import Animal
from random import randint  # импортируем функцию randint из модуля random


class Cat(Animal):
    """
    Класс, описывающий объект "кошка".
    """
    def __init__(self, name: str, preferred_food: set, age: int, treat_hours: int,
                 sleeping_hours: int, month: int) -> None:
        """
        Конструктор класса Cat.
        :param name: str - имя кошки.
        :param preferred_food: set - предпочитаемая еда кошки.
        :param age: int - возраст кошки.
        :param treat_hours: int - количество часов игры с кошкой.
        :param sleeping_hours: int - количество часов сна кошки.
        :param month: int - количество месяцев с последнего визита к ветеринару.
        """
        super().__init__(name, preferred_food, age, treat_hours, sleeping_hours, month)
        self.say_word = "Мяяяуу!"
        self.animal_type = "Кошка"

    def treat(self, hours: int = randint(0, 5)) -> str:
        """
        Метод, который запускает игру с кошкой.
        :param hours: Количество часов игры. По умолчанию - случайное число от 0 до 5.
        :return: Строка с наградой за игру с кошкой (мыши).
        """
        # если кошка не играет, то выводим сообщение об этом
        if self.treat_hours == 0:
            print(f'{self.name} не играет')
        else:
            # иначе выводим сообщение о количестве часов игры
            print(f'{self.name} играет {self.treat_hours} часа(ов)')
        return "Мертвых мышей :)"

    def sleeping(self, hours: int = randint(0, 5)) -> None:
        """
        Метод, который заставляет кошку спать.
        :param hours: Количество часов сна. По умолчанию - случайное число от 0 до 5.
        :return: Информация о сне кошки.
        """
        # Записываем количество часов сна кошки в атрибут класса
        self.sleeping_hours = hours
        # Выводим сообщение о количестве часов сна кошки и его качестве
        if self.sleeping_hours == 0:
            print(f'{self.name} не спит')
        elif self.sleeping_hours <= 3:
            print(f'{self.name} спит {self.sleeping_hours} час(а)(ов)! не выспался(ась) :(')
        elif self.sleeping_hours == 5:
            print(f'{self.name} спит {self.sleeping_hours} час(а)(ов)! очень хорошо поспал(а) :)')
        else:
            print(f'{self.name} спит {self.sleeping_hours} час(а)(ов)!')

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

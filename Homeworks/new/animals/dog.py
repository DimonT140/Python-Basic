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
        else:  # возвращаем сообщение о хорошем настроении
            print(f'Вы гуляете с {self.name} {self.treat_hours} час(а)(ов)!')
            return "Хорошее настроение"

    def sleeping(self, hours: int = randint(0, 5)) -> None:
        """
        Метод для сна собаки.
        :param hours: Количество часов сна. По умолчанию - случайное число от 0 до 5.
        :return: Информация о сне.
        """
        # если собака не спит, то выводим сообщение об этом
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

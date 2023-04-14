from time import sleep  # импортируем модуль sleep из библиотеки time
from typing import Set  # импортируем тип Set из модуля typing
from random import choices  # импортируем функцию choices из модуля random


class Cat:  # создаем класс Cat
    """
    Класс для представления кошки.
    """
    # метод __init__ для создания объекта класса
    def __init__(
            self, name: str, gender: str, age: int,
            breed: str, play_hours: int, preferred_food: Set[str], sleeping_hours: int
    ) -> None:
        """
        Рождение объекта класса/конструктор/инициализация.
        :param name: Имя кошки.
        :param gender: Пол кошки.
        :param age: Возраст кошки в годах.
        :param breed: Порода кошки.
        :param play_hours: Количество часов, которые кошка играет в день.
        :param preferred_food: Множество с предпочитаемой едой кошки.
        :param sleeping_hours: Количество часов, которые кошка спит в день.
        """
        # инициализируем свойства объекта
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed
        self.play_hours = play_hours
        self.preferred_food = preferred_food
        self.sleeping_hours = sleeping_hours
        self.hungry = False
        self.walked = False
        self.thirsty = False

    # получаем строковое представление объекта
    def __str__(self) -> str:
        """
        Метод для строкового представления объекта.
        :return: Строка, представляющая кошку.
        """
        # строка, представляющая кошку
        return f'{self.name}, {self.gender} пола, {self.age} лет, породы {self.breed.title()}'

    # заставляем кошку мяукнуть
    def mew(self) -> None:
        """
        Метод, который заставляет кошку мяукнуть.
        :return: выводит на экран имя кошки и то, что она мяукает
        """
        print(f'{self.name} мяукает!')

    # запускаем игру с кошкой
    def play(self) -> None:
        """
        Метод, который запускает игру с кошкой.
        """
        # если кошка не играет, то выводим  сообщение об этом
        if self.play_hours == 0:
            print(f'{self.name} не играет')
        else:
            # выводим сообщение о том, что кошка играет
            print(f'{self.name} играет {self.play_hours} часов!')
            # устанавливаем флаг "гуляла" в True и ждем 2 секунды
            self.walked = True
            print('Ждём...')
            sleep(2)
            # заставляем кошку мяукать
            self.mew()
            print('Мурлычет, потому что довольна!')

    # заставляем кошку спать
    def sleeping(self) -> None:
        """
        Метод, который заставляет кошку спать.
        """
        # если кошка не спит, то выводим сообщение об этом
        if self.sleeping_hours == 0:
            print(f'{self.name} не спит')
        else:
            # иначе выводим сообщение о количестве часов сна и ждём 2 секунды
            print(f'{self.name} спит {self.sleeping_hours} часов!')
            print('Ждём...')
            sleep(2)
            # генерируем событие пробуждения с равной вероятностью для еды и воды
            wake_up_event = choices(['eat', 'drink'], weights=[0.5, 0.5], k=1)[0]
            # если событие - еда, то кошка проснулась и хочет есть
            if wake_up_event == 'eat':
                print(f'{self.name} проснулась и хочет кушать')
                self.hungry = True
            # если событие - вода, то кошка проснулась и хочет пить
            else:
                print(f'{self.name} проснулась и хочет пить воду')
                self.thirsty = True

    # заставляем кошку есть
    def eat(self, suggested_food: str) -> None:
        """
        Метод, который заставляет кошку есть.
        :param suggested_food: Предложенная еда для кошки.
        """
        # если предложенная еда является предпочитаемой, то выводим сообщение о кормлении и кошка перестает быть голодной
        if suggested_food in self.preferred_food:
            print(f'{self.name} кушает {suggested_food}')
            self.hungry = False
        # если предложенная еда не является предпочитаемой, то выводим сообщение об этом и кошка продолжает быть голодной
        else:
            print(f'{self.name} предложили {suggested_food}, но мы такого не едим')

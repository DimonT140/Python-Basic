from cats import Cat  # импортируем класс Cat из модуля cats
from random import randint, choices  # импортируем функции randint и choices из модуля random

if __name__ == '__main__':
    # создаем экземпляры класса Cat для каждой кошки
    murzik = Cat('Мурзик', 'M', 4, 'дворняга', randint(0, 5), {'рыба', 'мясо', 'травка'}, randint(0, 5))
    chernysh = Cat('Черныш', 'M', 7, 'бомбей', randint(0, 5), {'сухой корм', 'консервы', 'мясо'}, randint(0, 5))
    pushok = Cat('Пушок', 'M', 3, 'ангора', randint(0, 5), {'сухой корм', 'сало', 'борщ'}, randint(0, 5))
    belka = Cat('Белка', 'Ж', 10, 'менуэт', randint(0, 5), {'травка', 'мясо', 'колбаса'}, randint(0, 5))
    murka = Cat('Мурка', 'Ж', 5, 'корат', randint(0, 5), {'рыба', 'сало', 'консервы'}, randint(0, 5))
    bagira = Cat('Багира', 'Ж', 2, 'бенгал', randint(0, 5), {'каша', 'консерва', 'колбаса'}, randint(0, 5))
    potential_food = ['рыба', 'мясо', 'травка', 'сухой корм', 'консервы', 'сало', 'борщ', 'каша', 'колбаса']
    # создаем список всех кошек и выводим его
    print("Наши киски:")
    print('', murzik, '\n', chernysh, '\n', pushok, '\n', belka, '\n', murka, '\n', bagira,)
    hungry_cats = list()  # создаем список голодных кошек
    cats_without_sleep = list()  # создаем список неспавших кошек
    cats_without_play = list()  # создаем список неигравших кошек
    # для каждой кошки в списке
    for cat in [murzik, chernysh, pushok, belka, murka, bagira]:  # итерация по списку котов
        print('=' * 20, f'\nОбычный день {cat}:')  # вывод строки с именем кота
        cat.mew()  # вызов метода "mew" у объекта-кота
        cat.play()  # вызов метода "play" у объекта-кота
        cat.sleeping()  # вызов метода "sleeping" у объекта-кота
        for food in choices(potential_food, k=2):  # итерация по списку еды
            cat.eat(food)  # вызов метода "eat" у объекта-кота, передача в него случайного значения из списка еды
        if cat.hungry:  # если кот голоден, то добавить его в список "hungry_cats"
            hungry_cats.append(cat)
        if cat.sleeping_hours == 0:  # если кот не спал, то добавить его в список "cats_without_sleep"
            cats_without_sleep.append(cat)
        if cat.play_hours == 0:  # если кот не играл, то добавить его в список "cats_without_play"
            cats_without_play.append(cat)
    if hungry_cats:  # если есть голодные коты
        print(f'\nНайдена(ы) {len(hungry_cats)} голодная(ые) киска(и), срочно покормите!')  # вывести количество голодных котов
        print('Вот их имена:', ', '.join([cat.name for cat in hungry_cats]))  # вывести имена голодных котов
    if cats_without_sleep:  # если есть коты, которые не спали
        print(f'\nНайдена(ы) {len(cats_without_sleep)} киска(и), которая(ые) не спала(и)')  # вывести количество котов, которые не спали
        print('Вот их имена:', ', '.join([cat.name for cat in cats_without_sleep]))  # вывести имена котов, которые не спали
    if cats_without_play:  # если есть коты, которые не играли
        print(f'\nНайдена(ы) {len(cats_without_play)} киска(и), которая(ые) не играла(и)')  # вывести количество котов, которые не играли
        print('Вот их имена:', ', '.join([cat.name for cat in cats_without_play]))  # вывести имена котов, которые не играли

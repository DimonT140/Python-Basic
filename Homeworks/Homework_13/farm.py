from animals import Dog, Hen, Cow, Cat
from random import choices, randint  # импортируем функцию choices и randint из модуля random


if __name__ == '__main__':
    # создаем список животных и добавляем в него экземпляры классов животных
    farm_animals = [
        Dog('Напас', {'мясо', 'сало', 'борщ'}, 14, randint(0, 5), randint(0, 5), randint(0, 5)),
        Hen('Ряба', {'пшено', 'крупа', 'вода'}, 2, randint(0, 5), randint(0, 5), randint(0, 5)),
        Cow('Бурёнка', {'трава', 'сено'}, 5, randint(0, 5), randint(0, 5), randint(0, 5)),
        Cat('Мурка', {'консервы', 'колбаса', 'сухой корм'}, 8, randint(0, 5), randint(0, 5), randint(0, 5))
    ]
    # создаем список доступной еды для животных
    food_to_offer = ['мясо', 'сало', 'борщ', 'пшено', 'крупа', 'вода', 'трава', 'сено', 'консервы', 'колбаса', 'сухой корм']
    animal_without_sleep = list()  # создаем список не спавших животных
    animal_without_treat = list()  # создаем список животных, о которых не заботились
    what_we_lost = list()  # создаем список потерь после ухода за животными
    what_we_get = list()  # создаем список приобретений после ухода за животными
    # перебираем всех животных в списке farm_animals
    for animal in farm_animals:
        print('\n', animal)  # выводим информацию о животном
        animal.last_vet_visit()  # вызываем метод "last_vet_visit" у каждого животного
        animal.say()  # вызываем метод "say" у каждого животного
        for food in choices(food_to_offer, k=3):  # выбираем три случайные еды из доступных
            animal.eat(food)  # вызываем метод "eat" у каждого животного для каждой еды
            what_we_lost.append(food)  # добавляем потерянную еду в список "what_we_lost"
        # вызываем метод "treat" у каждого животного и добавляем его результат в список "what_we_get"
        what_we_get.append(animal.treat())
        animal.sleeping()  # вызываем метод "sleeping" у каждого животного
        print()
        input("Нажмите enter, чтобы продолжить...")
    # проверяем каждое животное в списке farm_animals на голод и отсутствие сна
    for animal in farm_animals:
        if animal.hungry:
            print(f'На вашей ферме голодное животное! {animal}')
        if animal.sleeping_hours == 0:  # если животное не спало, то добавить его в список "animal_without_sleep"
            animal_without_sleep.append(animal)
        if animal.treat_hours == 0:  # если о животном не заботились, то добавить его в список "animal_without_treat"
            animal_without_treat.append(animal)
    if animal_without_sleep:  # если есть животные, которые не спали,
        # вывести количество животных, которые не спали
        print(f'\nНайдено(ы) {len(animal_without_sleep)} животное(ых), которое(ые) не спало(и)')
        # вывести имена животных, которые не спали
        print('Вот имя(ена):', ', '.join([animal.name for animal in animal_without_sleep]))
    else:
        print("Все животные спали")
    if animal_without_treat:  # если есть животные, о которых не заботились,
        # вывести количество животных, о которых не заботились
        print(f'\nНайдено(ы) {len(animal_without_treat)} животное(ых) о котором(ых) не заботились')
        # вывести имена животных, о которых не заботились
        print('Вот имя(ена):', ', '.join([animal.name for animal in animal_without_treat]))
    else:
        print("Вы заботились о всех животных")

    print(f'\nУхаживая за животными, мы потеряли: {what_we_lost}')
    print(f'Ухаживая за животными, мы получили: {what_we_get}')

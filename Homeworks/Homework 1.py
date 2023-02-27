# Program 1

import math
# Запрос ввода значения угла в градусах
degrees = float(input("Введите значение угла в градусах: "))
# Перевод градусов в радианы
radians = degrees * math.pi / 180
# Округление значения угла в радианах до 5 знака после запятой
rounded_radians = round(radians, 5)
# Вывод значения угла в радианах
print(f"{degrees} градусов = {rounded_radians} радиан")

# Program 2

# Вод показателей
previous_reading = float(input("Введите предыдущие показатели: "))
current_reading = float(input("Введите нынешние показатели: "))
rate = float(input("Введите тариф: "))
# Вычисление абонплаты
usage = current_reading - previous_reading
cost = usage * rate
# Вывод результата с округлением до 2 знака после запятой
print("Абонплата: {:.2f}".format(cost))

# Program 3

# Ввод данных
income = float(input("Введите размер постепления на счет, грн.: "))
tax_rate = float(input("Введите процентную ставку налога, %: "))
# Вычисления
tax_amount = income * (tax_rate / 100)
net_income = income - tax_amount
# Вывод результатов с округлением до 2 знака после запятой
print("Размер налога: {:.2f}".format(tax_amount))
print("Размер чистого дохода: {:.2f}".format(net_income))

# Program 4

# Ввод данных
fuel_consumption = float(input("Введите расход топлива на 100 км, л.: "))
fuel_price = float(input("Введите стоимость одного литра топлива, грн.: "))
distance = float(input("Ведите расстояние, которое нужно проехать, км.: "))
# Вычисления
fuel_needed = fuel_consumption * distance / 100
cost = fuel_needed * fuel_price
# Вывод результатов с округлением до 2 знака после запятой
print("Вартість палива: {:.2f}".format(cost))
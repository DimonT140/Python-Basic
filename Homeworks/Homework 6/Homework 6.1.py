import math


# функція конвертує градуси в радіани
def convert_degrees_to_radians(degree: float):
    radian = degree * math.pi / 180  # конвертуємо градуси в радіани
    rounded_radians = round(radian, 5)  # округлюємо результат до 5 знаків після коми
    return rounded_radians


if __name__ == '__main__':
    degrees = float(input("Введіть значення кута в градусах: "))  # запитуємо користувача про градуси
    radians = convert_degrees_to_radians(degrees)  # викликаємо функцію для конвертації

    # виводимо результат
    print(f"{degrees} градусів = {radians} радіан")

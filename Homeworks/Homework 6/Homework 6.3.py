from triangle import is_triangle_possible, calculate_perimeter, calculate_area


def read_side():
    # Зчитування сторони трикутника (додатнє число) та повернення цього значення
    while True:
        try:
            side = float(input('Введіть довжину сторони трикутника: '))
            if side > 0:
                return side
            else:
                print('Довжина сторони має бути додатнім числом.')
        except ValueError:
            print('Введіть додатнє число.')


if __name__ == '__main__':
    a = read_side()
    b = read_side()
    c = read_side()
    if is_triangle_possible(a, b, c):
        perimeter = calculate_perimeter(a, b, c)
        area = calculate_area(a, b, c)
        print(f"Для трикутника зі сторонами {a}, {b}, {c}:")
        print(f"Периметр дорівнює {perimeter:.2f}")
        print(f"Площа дорівнює {area:.2f}")
    else:
        print(f"Трикутник зі сторонами {a}, {b}, {c} не існує.")

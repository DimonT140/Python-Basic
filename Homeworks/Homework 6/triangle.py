import math


def is_triangle_possible(a, b, c):
    # Перевірка можливості існування трикутника та поверненням True/False
    return a + b > c and a + c > b and b + c > a


def calculate_perimeter(a, b, c):
    # Підрахунок периметру трикутника
    return a + b + c


def calculate_area(a, b, c):
    # Підрахунок площі трикутника
    s = calculate_perimeter(a, b, c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

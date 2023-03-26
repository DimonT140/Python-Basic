def fibonacci(n):
    """
    Функція-генератор послідовності чисел Фібоначчі
    :param n: Кінцевий індекс елементу послідовності.
    :yield: Числа послідовності по одному за кожен виклик.
    """
    a, b = 0, 1  # початкові значення для початку послідовності
    for i in range(n):  # генеруємо числа послідовності за допомогою циклу
        yield a  # повертаємо поточне число у послідовності
        a, b = b, a + b  # обчислюємо наступне число у послідовності та оновлюємо змінні

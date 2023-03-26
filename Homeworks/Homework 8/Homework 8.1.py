from fibonacci import fibonacci


if __name__ == '__main__':
    # запитуємо скільки чисел Фібоначчі вивести
    n = int(input("Скільки чисел Фібоначчі вивести? "))
    # використання функції-генератора для виведення чисел Фібоначчі до n
    for num in fibonacci(n):
        print(num)

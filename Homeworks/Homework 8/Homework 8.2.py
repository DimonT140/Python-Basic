from word_generator import word_gen


if __name__ == '__main__':
    s = input("Введіть рядок слів: ")  # просимо ввести рядок слів
    for word in word_gen(s):  # створюємо генератор і проходимо по кожному слову
        print(word)  # виводимо слово на екран

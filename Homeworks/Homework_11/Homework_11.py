import csv


def count_items(data, key):
    count_index = {}
    for row in data:
        item = row[key]
        if item not in count_index:
            count_index[item] = 1
        else:
            count_index[item] += 1
    for i, (item, count) in enumerate(count_index.items(), start=1):
        if key == 'brand':
            print(f'Від бренду "{item}" є {count} товарів')
        else:
            print(f'Серед категорії "{item}" є {count} товарів')
        if i % 8 == 0:
            input("\nНатисніть enter, щоб побачити продовження")
            print()


def get_items(data, key):
    value = input(f"\nПо якому/якій {key} вивести повну інформацію? \nабо натисніть enter, щоб пропустити \n")
    count = 0
    for item in data:
        if item[key] == value:
            print(item)
            count += 1
            if count % 8 == 0:
                input("\nНатисніть enter, щоб побачити продовження\n")


def show_brand_distribution(data):
    categories = set(item['category'] for item in data)
    for category in categories:
        brands = {}
        for item in data:
            if item['category'] == category:
                if item['brand'] in brands:
                    brands[item['brand']] += 1
                else:
                    brands[item['brand']] = 1
        print(f"У категорії \"{category}\" представлені товари таких брендів: {brands}")


def main():
    file_path = 'tech_inventory.csv'
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    count_items(data, 'brand')
    count_items(data, 'category')
    get_items(data, 'brand')
    get_items(data, 'category')
    show_brand_distribution(data)


if __name__ == '__main__':
    main()

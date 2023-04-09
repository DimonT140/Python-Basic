import csv


def main():
    file_path = 'tech_inventory.csv'
    brand_index = {}
    category_index = {}
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['category']
            brand = row['brand']
            data.append(row)
            if brand not in brand_index:
                brand_index[brand] = 1
            else:
                brand_index[brand] += 1
            if category not in category_index:
                category_index[category] = 1
            else:
                category_index[category] += 1

    for brand, count in brand_index.items():
        print(f'Від бренду "{brand}" є {count} товарів')
    print()
    for category, count in category_index.items():
        print(f'Серед категорії "{category}" є {count} товарів')
    print()

    brand = input("По якому бренду вивести повну інформацію? ")
    for item in data:
        if item['brand'] == brand:
            print(item)
    print()
    category = input("По якій категорії вивести повну інформацію? ")
    for item in data:
        if item['category'] == category:
            print(item)
    print()
    while True:
        category = input("введіть категорію або вихід): ")
        if category == 'вихід':
            break
        if category not in category_index:
            print(f'Категорії "{category}" не існує \n')
            continue
        brands = {}
        for item in data:
            if item['category'] == category:
                brand = item['brand']
                if brand not in brands:
                    brands[brand] = 1
                else:
                    brands[brand] += 1
        print(f'У категорії "{category}" представлені товари таких брендів: {brands} \n')


if __name__ == '__main__':
    main()

import requests
import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svyatoslav_shop.settings')
django.setup()
from shop.models import Product


def download_file(url_file, path):
    print('скачивание файла')
    r = requests.get(url_file)
    with open(path, 'w') as f:
        f.write(r.text)
    print(r.status_code)
    print(r.headers['content-type'])


def purchase_price(price) -> int:
    return int(price * 0.9)


def retail_price(price) -> int:
    if price < 1000:
        return int(price * 1.2)
    else:
        return int(price * 1.1)


def write_csv_to_db(file_obj):
    reader = csv.reader(file_obj, delimiter=";")
    prefix = "ПТ"
    count = 0
    product_list = []
    for row in reader:
        if count != 0:
            product_list.append(Product(article=prefix + row[0], name=row[1],
                                        purchase_price=purchase_price(int(row[2])),
                                        retail_price=retail_price(int(row[2]))))
             #print(f' Артикул {prefix+row[0]} Наим {row[1]} цена {int(row[2])} '
             #     f'закуп {purchase_price(int(row[2]))} розница {retail_price(int(row[2]))}')
        else:
            count += 1
    Product.objects.bulk_create(product_list)


if __name__ == '__main__':
    url = 'https://gist.githubusercontent.com/Wanderernk/1f3af500435bef872af2b6f3cc8e79fc/raw/' \
          '9b6862442f3fc516bd78a6adc6b550a01f970462/goods.csv'

    csv_path = "CSV/file.csv"

    # download_file(url, csv_path)

    with open(csv_path, "r") as f_obj:
        write_csv_to_db(f_obj)

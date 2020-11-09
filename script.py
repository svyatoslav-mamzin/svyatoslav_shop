import requests
import csv
from loguru import logger
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svyatoslav_shop.settings')
django.setup()
from shop.models import Product


@logger.catch
def download_file(url_file, path):
    logger.info('скачивание файла')
    r = requests.get(url_file)
    with open(path, 'w') as f:
        f.write(r.text)
    logger.debug(f'Статус-{r.status_code}')


def purchase_price(price):
    return price * 0.9


def retail_price(price):
    if price < 1000:
        return price * 1.2
    else:
        return price * 1.1


@logger.catch
def write_csv_to_db(file_obj):
    logger.info("Запись данных из файла в БД")
    reader = csv.reader(file_obj, delimiter=";")
    prefix = "ПТ"
    count = 0
    product_list = []
    for row in reader:
        if count != 0:
            product_list.append(Product(article=prefix + row[0], name=row[1],
                                        purchase_price=purchase_price(int(row[2])),
                                        retail_price=retail_price(int(row[2]))))
            # print(f' Артикул {prefix+row[0]} Наим {row[1]} цена {int(row[2])} '
            #     f'закуп {purchase_price(int(row[2]))} розница {retail_price(int(row[2]))}')
        else:
            count += 1
    try:
        Product.objects.bulk_create(product_list)
        logger.info("OK")
    except:
        logger.exception("oops")


if __name__ == '__main__':
    url = 'https://gist.githubusercontent.com/Wanderernk/1f3af500435bef872af2b6f3cc8e79fc/raw/' \
          '9b6862442f3fc516bd78a6adc6b550a01f970462/goods.csv'

    csv_path = "CSV/gods.csv"

    download_file(url, csv_path)


    with open(csv_path, "r") as f_obj:
        write_csv_to_db(f_obj)

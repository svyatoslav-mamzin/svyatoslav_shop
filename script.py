import requests
import csv


def download_file(url_file, path):
    print('скачивание файла')
    r = requests.get(url_file)
    with open(path, 'w') as f:
        f.write(r.text)
    print(r.status_code)
    print(r.headers['content-type'])


def purchase_price(price) -> int:
    return price * 0.9


def retail_price(price) -> int:
    if price < 1000:
        return price * 1.2
    else:
        return price * 1.1


def csv_reader(file_obj):
    reader = csv.reader(file_obj, delimiter=";")
    count = 0
    for row in reader:
        if count != 0:
            print(f' Артикул {row[0]} Наим {row[1]} цена {int(row[2])} '
                  f'закуп {purchase_price(int(row[2]))} розница {retail_price(int(row[2]))}')
        else:
            count += 1


if __name__ == '__main__':
    url = 'https://gist.githubusercontent.com/Wanderernk/1f3af500435bef872af2b6f3cc8e79fc/raw/' \
          '9b6862442f3fc516bd78a6adc6b550a01f970462/goods.csv'

    csv_path = "CSV/file.csv"

    # download_file(url, csv_path)

    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)

# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле,
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и
# общем времени выполнения программы.
import requests
import os
import time
import threading
import sys

urls = ['https://pichold.ru/wp-content/uploads/2018/10/maxresdefault-29-1.jpg',
        'https://www.zastavki.com/pictures/originals/2013/Animals___Dogs_Beautiful_eyes_beagle_dog_049972_.jpg',
        'https://proprikol.ru/wp-content/uploads/2021/01/sobachki-krasivye-kartinki-46.jpg',
        'https://proprikol.ru/wp-content/uploads/2021/01/krasivye-kartinki-sobak-31.jpg']


def download_image(url):
    start_time_download = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        filename = 'threads_' + url.split('/')[-1]
        path = os.path.join('images_threads', filename)  # Путь к папке "images" и имени файла
        os.makedirs('images_threads', exist_ok=True)  # Создание папки "images", если её не существует
        with open(path, 'wb') as file:
            file.write(response.content)
        end_time_download = time.time()
        print(f"Downloaded {filename} in {end_time_download - start_time_download} seconds")
    else:
        print(f"Failed to download {url}")


def multi_threaded_downloader(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")


if __name__ == "__main__":
    urls = sys.argv[1:]
    if not urls:
        print("Usage: python program.py <url1> <url2> ...")
        sys.exit(1)

    multi_threaded_downloader(urls)

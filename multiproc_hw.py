import requests
import os
import time
import multiprocessing
import sys

urls = ['https://pichold.ru/wp-content/uploads/2018/10/maxresdefault-29-1.jpg',
        'https://www.zastavki.com/pictures/originals/2013/Animals___Dogs_Beautiful_eyes_beagle_dog_049972_.jpg',
        'https://proprikol.ru/wp-content/uploads/2021/01/sobachki-krasivye-kartinki-46.jpg',
        'https://proprikol.ru/wp-content/uploads/2021/01/krasivye-kartinki-sobak-31.jpg']


def download_image(url):
    start_time_download = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        filename = 'multiproc_' + url.split('/')[-1]
        path = os.path.join('images_multiproc', filename)  # Путь к папке "images" и имени файла
        os.makedirs('images_multiproc', exist_ok=True)  # Создание папки "images", если её не существует
        with open(path, 'wb') as file:
            file.write(response.content)
        end_time_download = time.time()
        print(f"Downloaded {filename} in {end_time_download - start_time_download} seconds")
    else:
        print(f"Failed to download {url}")


def multiproc_downloader(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    urls = sys.argv[1:]
    if not urls:
        print("Usage: python program.py <url1> <url2> ...")
        sys.exit(1)

    multiproc_downloader(urls)
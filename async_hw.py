import aiohttp
import aiofiles
import asyncio
import os
import sys
import time

urls = ['https://pichold.ru/wp-content/uploads/2018/10/maxresdefault-29-1.jpg',
        'https://www.zastavki.com/pictures/originals/2013/Animals___Dogs_Beautiful_eyes_beagle_dog_049972_.jpg',
        'https://proprikol.ru/wp-content/uploads/2021/01/sobachki-krasivye-kartinki-46.jpg',
        'https://proprikol.ru/wp-content/uploads/2021/01/krasivye-kartinki-sobak-31.jpg']

async def download_image(url):
    start_time_download = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filename = 'async_' + url.split('/')[-1]
                path = os.path.join('images_async', filename)  # Путь к папке "images" и имени файла
                os.makedirs('images_async', exist_ok=True)  # Создание папки "images", если её не существует
                async with aiofiles.open(path, 'wb') as file:
                    await file.write(await response.read())
                end_time_download = time.time()
                print(f"Downloaded {filename} in {end_time_download - start_time_download} seconds")
            else:
                print(f"Failed to download {url}")

async def async_downloader(urls):
    start_time = time.time()
    tasks = [download_image(url) for url in urls]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    urls = sys.argv[1:]
    if not urls:
        print("Usage: python program.py <url1> <url2> ...")
        sys.exit(1)

    asyncio.run(async_downloader(urls))
import requests
import time
import threading

#For asyncio

import asyncio
import aiohttp

class ThreadingDownloader(threading.Thread):
    json_array = []
    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array


def get_data_threading(urls):
    sttime = time.time()

    #threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        #threads.append(t)

    #for t in threads:
        #t.join()
        #print(t)

    endtime = time.time()
    elapsed_time = endtime - sttime
    print(f"Execution time {elapsed_time}")

async def get_data_async_but_as_wrapper(urls):
    sttime = time.time()

    json_array = []

    async with aiohttp.ClientSession() as session: # bir session oluşturma async ile
        for url in urls:
            async with session.get(url) as response:
                json_array.append(await response.json())

    endtime = time.time()
    elapsed_time = endtime - sttime
    print(f"Execution time {elapsed_time}")
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 10
#asyncio.run(get_data_async_but_as_wrapper(urls))#bu şekilde çalıştırılması gerekiyor#33 sny de yaptı
#get_data_threading(urls)#4sny
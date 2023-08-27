import threading
#çekirdeklere yüklenmeden işlem yapmak amacımız
import requests
import time

def get_data_sync(urls):
    started_time = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    end_time = time.time()
    elapsed_time = end_time - started_time
    print(f"Gecen süre : {elapsed_time}")
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 10
get_data_sync(urls)
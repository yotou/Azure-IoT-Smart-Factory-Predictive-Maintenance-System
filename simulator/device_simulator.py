import random
import time
import requests

API_URL = "http://localhost:5000/data"

while True:
    data = {
        "temperature": random.uniform(20, 100),
        "vibration": random.uniform(0, 10)
    }

    print("Sending:", data)

    try:
        requests.post(API_URL, json=data)
    except:
        print("API not running yet")

    time.sleep(2)
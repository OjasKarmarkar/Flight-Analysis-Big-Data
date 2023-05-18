import json
from datetime import datetime
import urllib.request
from urllib.request import Request, urlopen
import time
from kafka import KafkaProducer

API_KEY = "4e0ee82a-1406-4fbe-8df0-ee28c8c15251"

url = "https://airlabs.co/api/v9/flights?api_key={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:

 response = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'})
 flights = json.loads(urlopen(response).read().decode())


 for flight in flights["response"]:
   producer.send("flight-realtime", json.dumps(flight).encode())

 print("{} Produced {} station records".format(datetime.now(), len(flights['response'])))

 time.sleep(1)

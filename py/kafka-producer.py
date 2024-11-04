from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sensors = ['Sensor_1', 'Sensor_2', 'Sensor_3']

try:
    while True:
        for sensor_id in sensors:
            temperature = random.randint(60, 100)
            data = {'sensor_id': sensor_id, 'temperature': temperature}
            producer.send('sensor-suhu', value=data)
            print(f"Sent data: {data}")
        time.sleep(1) 
except KeyboardInterrupt:
    print("Stopping producer.")
    producer.close()

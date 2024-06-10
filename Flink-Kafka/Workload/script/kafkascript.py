from kafka import KafkaProducer
import json
import random
import time
import uuid
import requests


#Initialize the Kafka producer
producer = KafkaProducer(bootstrap_servers=['kafka-kafka-bootstrap.default.svc.cluster.local:9092'])

# Function to generate a random IP address
def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Function to generate a random event type
def random_event_type():
    return random.choice(["display", "click"])

# Function to create a random message
def create_message():
    return {
        "impressionId": str(uuid.uuid4()),
        "ip": random_ip(),
        "uid": str(uuid.uuid4()),
        "timestamp": int(time.time()),
        "eventType": random_event_type()
    }

# Function to produce a message to Kafka
def produce_message(topic):
    message = create_message()
    producer.send(topic, json.dumps(message).encode('utf-8'))
    producer.flush()
    
# Main function to send messages continuously
def main():
    topic = 'transactions'
    sleep_time = 0.5 #choose sleep time
    start_time = time.time()

    while True:
        produce_message(topic)
        elapsed_time = time.time() - start_time
        if elapsed_time >= 30:  
            sleep_time /= 2
            start_time = time.time()  # Reset the start time
            if sleep_time < 0.01:
                sleep_time = 0.01
                break  # Exit the loop when sleep time reaches desired value
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()

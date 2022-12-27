import subprocess
from kafka import KafkaProducer

def ping(host):
    result = subprocess.run(['ping', '-c', '3', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    return result.stdout

def parse_ping_output(output):
    latencies = []
    for line in output.split('\n'):
        if 'time=' in line:
            latency = float(line.split('time=')[1].split(' ')[0])
            latencies.append(latency)
    return latencies

def publish_to_kafka(latencies):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    topic = 'ping-results'
    for latency in latencies:
        producer.send(topic, str(latency).encode())
    producer.flush()

output = ping('www.google.com')
latencies = parse_ping_output(output)
publish_to_kafka(latencies)
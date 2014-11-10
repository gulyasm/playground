import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
for _ in range(5):
    channel.basic_publish(exchange='', routing_key="hello", body="Hello world!")
connection.close()


import pika
import time
import json

import connect
from models import Contact


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='sms', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def some_work(id):
    time.sleep(2)   #do some work 
    con = Contact.objects.get(id = id)
    con.logic = True
    con.save()


def callback(ch, method, properties, body):
    message = body.decode()
    print(f" [x] Received sms{message}")
    some_work(message)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='sms', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
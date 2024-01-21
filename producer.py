import pika
import sys
import json
from faker import Faker
from datetime import datetime

import connect
from models import Contact


fake = Faker()
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.confirm_delivery()
channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')


def seed():
    for _ in range(20):
        id = Contact(
            fullname = fake.name() ,
            email = fake.email(),
            logic = False
        ).save()
        # print(id.id)


def sender():        
    for id in Contact.objects():
        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=str(id.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % str(id.id))
    connection.close()
    
    
if __name__ == '__main__':
    seed()
    sender()

    
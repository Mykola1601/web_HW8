import pika
import json
from faker import Faker
from datetime import datetime
import random
import connect
from models import Contact


fake = Faker()
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.confirm_delivery()
channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='sms', durable=True)
channel.queue_declare(queue='email', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')


def seed(num):
    for _ in range(num):
        id = Contact(
            fullname = fake.name() ,
            phone = fake.phone_number() ,
            email = fake.email(),
            method = random.choice(["sms", "email"]),
            logic = False
        ).save()


def sender():        
    for obj in Contact.objects():
        body=str(obj.id).encode()
        if obj.method == "sms":
            channel.basic_publish(exchange='task_mock', routing_key='sms', body=body)
        if obj.method == "email":
            channel.basic_publish(exchange='task_mock', routing_key='email', body=body)
        print(" [x] Sent %r" % str(obj.id))
    connection.close()
    
    
if __name__ == '__main__':
    seed(50)
    sender()

    
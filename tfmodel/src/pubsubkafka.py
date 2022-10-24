from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps

addr_broker = ['broker:29092', 'localhost:9092']


class PubSubKafka:
    topic_cons = 'hotelc'
    consumer = KafkaConsumer(topic_cons,
                             bootstrap_servers=addr_broker,
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             value_deserializer=lambda m: loads(m.decode('utf-8'))
                             )
    producer = KafkaProducer(bootstrap_servers=addr_broker,
                             value_serializer=lambda v: dumps(v).encode('utf-8'))

    def send_reply(self, hotelc, result):
        event = {
            'session': hotelc['session'],
            'result': result
        }

        self.producer.send(f'{hotelc["session"]}-hotelresult', event)

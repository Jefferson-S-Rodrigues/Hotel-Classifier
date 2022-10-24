from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps

addr_broker = ['broker:29092', 'localhost:9092']


def get_result(hotel_class):
    consumer_result = KafkaConsumer(f'{hotel_class["session"]}-hotelresult',
                                    bootstrap_servers=addr_broker,
                                    auto_offset_reset='earliest',
                                    enable_auto_commit=True,
                                    value_deserializer=lambda m: loads(m.decode('utf-8'))
                                    )
    for reply in consumer_result:
        return reply.value


class PubSubKafka:
    topic_cons = 'toservices'
    topic_hotel = 'hotelc'
    consumer_result = None
    consumer = KafkaConsumer(topic_cons,
                             bootstrap_servers=addr_broker,
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             value_deserializer=lambda m: loads(m.decode('utf-8')))
    producer = KafkaProducer(bootstrap_servers=addr_broker,
                             value_serializer=lambda v: dumps(v).encode('utf-8'))

    def send_hotel_class(self, hotel_class):
        self.producer.send(self.topic_hotel, hotel_class)

    def send_reply(self, hotel_class, result):
        event = {
            'session': hotel_class['session'],
            'result': result
        }

        self.producer.send(f'{hotel_class["session"]}-servicesresult', event)

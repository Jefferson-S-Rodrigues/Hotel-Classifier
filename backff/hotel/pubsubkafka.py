from datetime import datetime
from json import dumps, loads

from kafka import KafkaProducer, KafkaConsumer

addr_broker = ['broker:29092', 'localhost:9092']


def get_result(session):
    consumer_result = KafkaConsumer(f'{session}-servicesresult',
                                    bootstrap_servers=addr_broker,
                                    auto_offset_reset='earliest',
                                    enable_auto_commit=True,
                                    value_deserializer=lambda m: loads(m.decode('utf-8'))
                                    )
    for hotelresult in consumer_result:
        return hotelresult.value


class PubSubKafka:
    topic_cons = 'toservices'
    producer = KafkaProducer(bootstrap_servers=addr_broker,
                             value_serializer=lambda v: dumps(v).encode('utf-8'))

    def send_services(self, flag, hoteldata, session):
        hotel_message = {'flagcur': flag, 'session': session}
        if flag == "realize_class":
            hotel_message['hoteldata'] = hoteldata
            hotel_message['tshotel'] = str(datetime.now())
        self.producer.send(self.topic_cons, hotel_message)

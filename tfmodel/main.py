import json

from src.pubsubkafka import PubSubKafka as PSK
from src.hotelanalyzer import Hotel as HA

if __name__ == '__main__':
    psk = PSK()
    ha = HA()
    
    for msg in psk.consumer:
        msgrequest = msg.value

        hoteldata = json.loads(msgrequest['hoteldata'])

        result = ha.find_similar_hotels(hoteldata)

        print(f"Result: {result}")
        psk.send_reply(msgrequest, result)

        print("Reply")

from dbservice import register_use
from pubsubkafka import PubSubKafka as PSK, get_result

if __name__ == '__main__':

    psk = PSK()
    for msg in psk.consumer:
        hotel_request = msg.value
        print(hotel_request)

        if hotel_request['flagcur'] == "realize_class":
            psk.send_hotel_class(hotel_request)

            print("Sent to model")

            hotel_result = get_result(hotel_request)

            psk.send_reply(hotel_request, hotel_result)
            print("Reply")

            register_use(hotel_request)
            print("Saved")

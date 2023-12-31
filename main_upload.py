import main_read
import time
from AWS import aws_iot_core_connect

bus = main_read.bus_start()
main_read.collect_start(bus)
time.sleep(1)

timestamp = time.time()
clientId = 1
gas = 0
temp_comp = main_read.collect_temp(bus)
hum_comp = main_read.collect_humid(bus, temp_comp)

message_topic = "pp/home/air/add"
message_dict = {
    "timestamp": timestamp,
    "client": clientId,
    "gas": gas,
    "humid": hum_comp/10000,
    "temp": temp_comp/100
}

try:
    client = aws_iot_core_connect.client_create_and_connect()
    aws_iot_core_connect.client_publish_message(client, message_topic, message_dict)
except Exception as e:
    print(e)
finally:
    aws_iot_core_connect.client_stop(client)
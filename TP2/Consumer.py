from kafka import KafkaConsumer, TopicPartition
from time import sleep
from BankAccount import BankAccount

#Consumer
id_consumer = "Consumer-Vinicius"
servers = ['localhost:19092']
topic = "patinho2"
partition_control = 0
partition_content = 1

tp_content = [TopicPartition(topic, partition_content)]
tp_control = [TopicPartition(topic, partition_control)]
consumer = KafkaConsumer(bootstrap_servers=servers, auto_offset_reset= 'earliest')


# obtain the last offset value
consumer.assign(tp_content)
consumer.seek_to_end(tp_content[0])
lastOffset = consumer.position(tp_content[0])
consumer.seek_to_beginning(tp_content[0])
sleep(1)

for message in consumer:
    print("___")
    print("Offset:", message.offset)
    print("Value:", message.value)
    if message.offset == lastOffset - 1:
        break

# obtain the last offset value
consumer.seek_to_end(tp_control)
lastOffset = consumer.position(tp_control[1])
consumer.seek_to_beginning(tp_control[1])
requests = []  
for message in consumer:
    print("Offset:", message.offset)
    print("Value:", message.value)
    requests.append(message.value.decode().split(":"))

    if message.offset == lastOffset - 1:
        break


print(requests)

from kafka import KafkaProducer
import json
import time
import random
import pandas as pd

pd.options.display.max_columns = 100

# wir laden die Daten aus der CSV-Datei in ein Pandas DataFrame
data = pd.read_csv('data/de_challenge_sample_data.csv')

#print(data.head(10))
#print(data.columns)

# Wir erstellen eine KafkaProducer-Instanz mit der Adresse des Kafka-Brokers
producer = KafkaProducer(bootstrap_servers="kafka-challenge-kafka-1:9092")

# Diese Funktion wird aufgerufen, wenn eine Nachricht erfolgreich gesendet wurde
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


# Wir iterieren durch jede Zeile im Dataframe, bei jedem Durchlauf wird die Zeile zrückgegeben
for _, row in data.iterrows():
    # Sende die Nachricht an das Kafka-Topic mit 'edit' als Schlüssel
    # die Zeile wird zu einem Dictionary konvertiert und dann durch json.dumps() in JSON format umgewandelt
    producer.send('wikipedia-changes', key='edit', value=json.dumps(row.to_dict())).add_callback(delivery_report)

    # Warte für eine zufällige Zeit zwischen 0 und 1 Sekunde
    time.sleep(random.uniform(0, 1))

# Warte, um sicherzustellen, dass alle Nachrichten gesendet wurden
producer.flush()







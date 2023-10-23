from kafka import KafkaConsumer
from collections import defaultdict
import json


# Herstellung der Verbindung zum Kafka-Cluster und abonnieren das Topic wikipedia-changes
consumer = KafkaConsumer("wikipedia-changes", bootstrap_servers="localhost:9092", group_id="wiki-edits-group")

global_edits_per_minute = defaultdict(int)
german_edits_per_minute = defaultdict(int)

previous_minute = None # initialisierung von der vorherigen Minute (um den Unterschied zwischen der aktuellen Minute und vorherigen Minute zu machen)

for message in consumer:
    data = json.loads(message.value.decode("utf-8"))
    # wir greifen auf den Value von timestamp
    timestamp = data["timestamp"]

    # wir extrahieren  die Sprache aus der Domäne, um die deutsche Wikipedia identifizieren zu können
    if "de.wikipedia.org" in data["meta_domain"]:
        german_wikipedia = True
    else:
        german_wikipedia = False

    # wir ermitteln die Minute des Timestamps
    minute = timestamp // 60

    # Wenn es eine neue Minute ist, wird die Zählungen aktualisiert
    if minute != previous_minute:
        global_edits_per_minute[minute] = 1
        if german_wikipedia:
            german_edits_per_minute[minute] = 1
        previous_minute = minute   # hier wird die vorherige Minute auf die aktuelle Minute aktualisiert
    else:
        global_edits_per_minute[minute] += 1
        if german_wikipedia:
            german_edits_per_minute[minute] += 1

    # Ausgabe von golaben und deutschen Edits
    print(f"Global Edits Per Minute: {global_edits_per_minute}")
    print(f"German Wikipedia Edits Per Minute: {german_edits_per_minute}")



from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(bootstrap_servers="kafka-challenge-kafka-1:9092")
topic = NewTopic(name="wikipedia-changes", num_partitions=1, replication_factor=1)
admin_client.create_topics([topic])


from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='test'
)

topic_name = "sensor-suhu"
topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)

try:
    admin_client.create_topics(new_topics=[topic], validate_only=False)
    print(f"Topic '{topic_name}' created.")
except Exception as e:
    print(f"Error creating topic: {e}")

topics = admin_client.list_topics()
print("Existing topics:", topics)

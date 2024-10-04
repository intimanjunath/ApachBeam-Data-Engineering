import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.kafka import ReadFromKafka, WriteToKafka
import json


# Define a function to process the data
def process_message(message):
    key, value = message
    return (key.decode("utf-8"), value.decode("utf-8"))


# Kafka configuration
kafka_consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "beam-group",
}

kafka_producer_config = {
    "bootstrap.servers": "localhost:9092",
}

input_topic = "your-input-topic"
output_topic = "your-output-topic"

# Pipeline options
pipeline_options = PipelineOptions(
    streaming=True  # Enable streaming mode
)

# Create the Beam pipeline
with beam.Pipeline(options=pipeline_options) as pipeline:
    # Read from Kafka
    kafka_messages = (
        pipeline
        | "Read from Kafka"
        >> ReadFromKafka(
            consumer_config=kafka_consumer_config,
            topics=[input_topic],
            key_deserializer="org.apache.kafka.common.serialization.ByteArrayDeserializer",
            value_deserializer="org.apache.kafka.common.serialization.ByteArrayDeserializer",
        )
        | "Process Messages" >> beam.Map(process_message)
    )

    # Write to Kafka
    kafka_messages | "Write to Kafka" >> WriteToKafka(
        producer_config=kafka_producer_config,
        topic=output_topic,
        key_serializer="org.apache.kafka.common.serialization.StringSerializer",
        value_serializer="org.apache.kafka.common.serialization.StringSerializer",
    )

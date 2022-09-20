import os
import json
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError


class GcpPubsub(object):
    def __init__(self):
        # GCP topic, project & subscription ids
        self.PUB_SUB_TOPIC = (
            "sui-dev"
            if os.environ.get("PUB_SUB_TOPIC") == None
            else os.environ["PUB_SUB_TOPIC"]
        )
        self.PUB_SUB_PROJECT = (
            "sui-data-ingestion-devnet" "sui-dev"
            if os.environ.get("PUB_SUB_PROJECT") == None
            else os.environ["PUB_SUB_PROJECT"]
        )
        self.PUB_SUB_SUBSCRIPTION = (
            "sui-dev-sub" "sui-dev"
            if os.environ.get("PUB_SUB_SUBSCRIPTION") == None
            else os.environ["PUB_SUB_SUBSCRIPTION"]
        )

    def process_payload(self, message):
        print(f"Received {message.data}.")
        message.ack()

    # producer function to push a message to a topic
    def push_payload(self, payload):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.PUB_SUB_PROJECT, self.PUB_SUB_TOPIC)

        print(payload.replace("\\", ""))
        data = json.dumps(payload).encode("utf-8")
        future = publisher.publish(topic_path, data=data)
        print("Pushed message to topic.")

    # consumer function to consume messages from a topics for a given timeout period
    def consume_payload(self, callback, period):
        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscriber.subscription_path(
            self.PUB_SUB_PROJECT, self.PUB_SUB_SUBSCRIPTION
        )
        
        print(f"Listening for messages on {subscription_path}..\n")

        streaming_pull_future = subscriber.subscribe(
            subscription_path, callback=callback
        )
        # Wrap subscriber in a 'with' block to automatically call close() when done.
        with subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                streaming_pull_future.result(timeout=period)
            except TimeoutError:
                streaming_pull_future.cancel()

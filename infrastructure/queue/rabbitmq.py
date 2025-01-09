import pika


class RabbitMQ:
    """
    A class responsible for managing communication with a RabbitMQ message queue.

    This class handles the connection, publishing messages, and consuming messages from a specified RabbitMQ queue.

    Attributes:
        queue_name (str): The name of the queue to interact with (default is 'pdf_queue').
        connection (pika.BlockingConnection): The connection object used to communicate with RabbitMQ.
        channel (pika.BlockingChannel): The channel object used to send and receive messages from the RabbitMQ queue.
    """

    def __init__(self, queue_name='pdf_queue'):
        """
        Initializes the RabbitMQ connection and declares a queue for message communication.

        Args:
            queue_name (str): The name of the queue (default is 'pdf_queue').
        """
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def _connect(self):
        """Establishes a connection with RabbitMQ and sets a heartbeat."""
        params = pika.ConnectionParameters(
            host='rabbitmq',
            heartbeat=30,
            blocked_connection_timeout=300,
        )
        return pika.BlockingConnection(params)

    def send(self, message):
        """
        Sends a message to the specified RabbitMQ queue.

        Args:
            message (str): The message to be sent to the queue.

        Prints a confirmation message indicating that the message has been sent.
        """
        try:
            self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
            print(f"Sent: {message}")
        except Exception as e:
            print("Stream connection lost. Reconnecting...")
            self.connection = self._connect()
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name)
            self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)

    def consume(self, callback):
        """
        Consumes messages from the specified RabbitMQ queue and processes them using the given callback.

        This method starts listening for messages on the queue and invokes the provided callback
        function to handle each message when it arrives.

        Args:
            callback (function): A callback function to be invoked when a message is received.

        Prints a message indicating that it is waiting for messages and starts consuming them.
        """
        try:
            self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
            print(f"Waiting for messages on queue: {self.queue_name}")
            self.channel.start_consuming()
        except Exception as e:
            print("Stream connection lost. Reconnecting...")
            self.connection = self._connect()
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name)
            self.consume(callback)
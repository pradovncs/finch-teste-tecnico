import os

from flask import request
from infrastructure.queue.rabbitmq import RabbitMQ


class PDFController:
    """
    A controller class for handling PDF file uploads and sending them for processing.

    This class allows users to upload PDF files, save them to the local storage, and
    send their paths to a RabbitMQ queue for further processing.
    """

    def __init__(self):
        """
        Initializes the PDFController class by creating an instance of RabbitMQ.

        Sets up the connection to the RabbitMQ queue that will handle the processing
        of uploaded files.
        """
        self.queue = RabbitMQ()

    def upload_files(self):
        """
        Handles the upload of PDF files from the request.

        This method retrieves the uploaded PDF files, saves them to the 'uploads' directory,
        and sends their file paths to the RabbitMQ queue for processing.

        Returns:
            str: A message indicating that the files have been sent for processing.
        """
        files = request.files.getlist('files[]')
        for file in files:
            if file.filename.endswith('.pdf'):
                upload_dir = 'uploads'
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)

                file_path = os.path.join(upload_dir, file.filename)
                file.save(file_path)
                self.queue.send(file_path)

        return ("Files have been sent for processing. "
                "The output will be available on your desktop as 'processos.xlsx'.")
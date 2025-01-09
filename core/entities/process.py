class Process:
    """
    A class that represents a legal process with associated details.

    This class stores information about a legal process, such as the file path,
    author and defendant names, process number, process value, sentence date,
    and vehicle details (plate and model). It also provides a method to convert
    the instance into a dictionary format for easier data handling.
    """

    def __init__(self, file_path, author_name=None, process_number=None, defendant_name=None, process_value=None,
                 sentence_date=None, vehicle_plate=None, vehicle_model=None):
        """
        Initializes a new instance of the Process class.

        Args:
            file_path (str): The path to the file related to the legal process.
            author_name (str, optional): The name of the process author. Defaults to None.
            process_number (str, optional): The process number. Defaults to None.
            defendant_name (str, optional): The name of the defendant. Defaults to None.
            process_value (float, optional): The value of the process. Defaults to None.
            sentence_date (str, optional): The date the sentence was issued. Defaults to None.
            vehicle_plate (str, optional): The vehicle's plate number. Defaults to None.
            vehicle_model (str, optional): The model of the vehicle involved in the process. Defaults to None.
        """
        self.file_path = file_path
        self.author_name = author_name
        self.defendant_name = defendant_name
        self.process_number = process_number
        self.process_value = process_value
        self.sentence_date = sentence_date
        self.vehicle_plate = vehicle_plate
        self.vehicle_model = vehicle_model

    def to_dict(self):
        """
        Converts the Process instance to a dictionary format.

        This method returns the process details as a dictionary, making it easier
        to handle and serialize the data.

        Returns:
            dict: A dictionary representation of the process with keys such as 'autor',
                  'reu', 'numero_processo', 'valor_indenizacao', 'data_sentenca',
                  'placa', and 'veiculo'.
        """
        return {
            "arquivo": self.file_path,
            "autor": self.author_name,
            "reu": self.defendant_name,
            "numero_processo": self.process_number,
            "valor_indenizacao": self.process_value,
            "data_sentenca": self.sentence_date,
            "placa": self.vehicle_plate,
            "veiculo": self.vehicle_model,
        }
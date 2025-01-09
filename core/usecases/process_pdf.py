from core.entities.process import Process
from infrastructure.pdf_processing.pdf_extractor import PDFExtractor

class ProcessPDFUseCase:
    """
    A use case that handles the extraction of process data from a PDF file and
    converts it into a Process entity.

    This class uses a PDFExtractor to extract specific data from a PDF and creates
    a Process instance with the extracted details.
    """

    def __init__(self, extractor: PDFExtractor):
        """
        Initializes the ProcessPDFUseCase instance with a PDFExtractor.

        Args:
            extractor (PDFExtractor): An instance of the PDFExtractor class used
                                        to extract data from the PDF files.
        """
        self.extractor = extractor

    def execute(self, file_path):
        """
        Extracts data from the provided PDF file and returns a Process instance.

        This method uses the extractor to parse the PDF and then constructs a
        Process object containing the extracted data such as author, defendant,
        process number, process value, sentence date, vehicle plate, and vehicle model.

        Args:
            file_path (str): The path to the PDF file to be processed.

        Returns:
            Process: An instance of the Process class populated with the extracted data.
        """
        data = self.extractor.extract(file_path)
        return Process(
            file_path=file_path,
            author_name=data.get("autor"),
            defendant_name=data.get("reu"),
            process_number=data.get("numero_processo"),
            process_value=data.get("valor_indenizacao"),
            sentence_date=data.get("data_sentenca"),
            vehicle_plate=data.get("placa"),
            vehicle_model=data.get("veiculo"),
        )
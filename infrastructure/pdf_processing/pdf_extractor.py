import pdfplumber
import re

patterns = {
    "autor": r"Requerente:\s*([\w\s]+)",
    "reu": r"Requerido:\s*([\w\s]+)",
    "numero_processo": r"Processo Digital nº:\s*(\S+)",
    "valor_indenizacao": r"indenização por danos morais\s*em\s*R\$\s*([\d\.,]+)",
    "data_sentenca": r"\b(\d{1,2}\s+de\s+\w+\s+de\s+\d{4})\b",
    "placa": r"placas\s*([\w\d]+)",
    "veiculo": r"veículo marca\s*([\w\s]+),\s*modelo\s*([\w\s]+)",
}

class PDFExtractor:
    """
    A class responsible for extracting data from a PDF file based on predefined patterns.

    This class uses regular expressions to match and extract specific information
    from the text content of a PDF file, such as the author, defendant, process number,
    indemnity value, sentence date, vehicle plate, and vehicle model.
    """

    @staticmethod
    def extract(file_path):
        """
        Extracts specific data from a given PDF file.

        This method reads the content of a PDF file, applies regular expressions to
        extract predefined pieces of information, and returns the results in a dictionary.

        Args:
            file_path (str): The path to the PDF file from which data is to be extracted.

        Returns:
            dict: A dictionary containing the extracted data, where keys are the data fields
                  (e.g., 'autor', 'reu', etc.) and values are the extracted values.
                  If a match is not found, the value will be None.
        """
        with pdfplumber.open(file_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text()

        extracted_data = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, full_text)
            extracted_data[key] = match.group(1) if match else None


        print(extracted_data)
        return extracted_data
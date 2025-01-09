import pandas as pd

OUTPUT_DIR = "/app/output/processos.xlsx"

class ExcelPresenter:
    """
    A class responsible for presenting processed data and saving it to an Excel file.

    This class contains methods for converting processed data into a DataFrame
    and saving it to an Excel file in the specified output directory.
    """

    @staticmethod
    def save_to_excel(processed_data):
        """
        Converts the processed data into an Excel file.

        This method takes the processed data, converts it into a pandas DataFrame,
        and then saves it as an Excel file at the specified output directory.

        Args:
            processed_data (list): A list of processed data objects to be saved to Excel.

        Returns:
            None: The method saves the data to a file and does not return any value.
        """
        df = pd.DataFrame([data.to_dict() for data in processed_data])
        output_file = OUTPUT_DIR
        df.to_excel(output_file, index=False)
        print(f"Data saved to {output_file}")
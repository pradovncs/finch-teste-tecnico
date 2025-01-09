from core.usecases.process_pdf import ProcessPDFUseCase
from infrastructure.queue.rabbitmq import RabbitMQ
from infrastructure.pdf_processing.pdf_extractor import PDFExtractor
from app.presenters.excel_presenter import ExcelPresenter

MAX_FILES = 5

processed_files = []

def process_message(ch, method, properties, body):
    file_path = body.decode()
    print(file_path)
    use_case = ProcessPDFUseCase(PDFExtractor())
    processed_files.append(use_case.execute(file_path))

    if len(processed_files) <= MAX_FILES:
        ExcelPresenter.save_to_excel(processed_files)


queue = RabbitMQ()
queue.consume(process_message)
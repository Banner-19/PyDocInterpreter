# For PDF
import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(reader.getNumPages()):
            text += reader.getPage(page).extract_text()
        return text
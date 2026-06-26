import os

from loaders.pdf_loader import load_pdf
from loaders.docx_loader import load_docx
from loaders.txt_loader import load_txt
from loaders.csv_loader import load_csv
from loaders.ppt_loader import load_ppt
from loaders.excel_loader import load_excel


LOADERS = {
    ".pdf": load_pdf,
    ".docx": load_docx,
    ".txt": load_txt,
    ".csv": load_csv,
    ".pptx": load_ppt,
    ".xlsx": load_excel,
}


def load_document(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension not in LOADERS:
        raise ValueError(f"Unsupported file: {extension}")

    return LOADERS[extension](file_path)
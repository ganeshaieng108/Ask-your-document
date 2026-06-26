import pandas as pd
from langchain_core.documents import Document

def load_excel(file_path):
    sheets = pd.read_excel(file_path, sheet_name=None)

    documents = []

    for sheet_name, df in sheets.items():
        text = df.to_string(index=False)

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "sheet": sheet_name,
                    "source": file_path
                }
            )
        )

    return documents
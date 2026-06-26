from langchain_community.document_loaders import UnstructuredPowerPointLoader

def load_ppt(file_path):
    loader = UnstructuredPowerPointLoader(file_path)
    return loader.load()
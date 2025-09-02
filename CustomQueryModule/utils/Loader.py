from langchain.document_loaders import PyPDFLoader
from langchain_core.documents.base import Document



def PDFLoader(path:str) -> list[Document] :
    loader = PyPDFLoader(path)
    data = loader.load()
    return data
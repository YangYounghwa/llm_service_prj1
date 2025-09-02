from .utils import APIKEY
from langchain.document_loaders import PDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter,CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI

class QueryService:
    
    splitted_docs = None
    vectorStore = None
    chat = None
    
    def __init__(self):
        """
        APIKEY loader. 
        Default key is from dotenv.
        """
        key = APIKEY()
        key.setKeyFromEnv()
        print("Default API_KEY loaded.")
        # print(key.getOPENAI_API_KEY())
        pass
        
    def setKey(self,keys:dict):
        """_summary_
        Set keys to key.
        Args:
            keys (dict): _description_
        """
        if('OPENAI_API_KEY' in keys.keys()):
            self.key.setOPENAI_API_KEY( keys.get('OPENAI_API_KEY')) 
        # Check more keys if needed  
    def getKeyObject(self)->APIKEY:
        return self.key
    def getOPENAI_API_KEY(self)-> str:
        return self.key.getOPENAI_API_KEY() (self)
 
    def LoadDocuments(self,path:str,docType:str,split_method:str = "recursive")->None:
        documents = None
        if(docType == "pdf"):
            documents= PDFLoader(path)
        # if(docType == "txt"):
        #     self.documents= TXTLoader(path)
        if (split_method=="recursive"):
            recursive_splitter = RecursiveCharacterTextSplitter(
                chunk_size=450,
                chunk_overlap=50,
                separators=["\n\n", "\n", " ", ""],
                length_function=len
            ) 
        
            splitted_docs= recursive_splitter.split_documents(documents)
            # print(recursive_docs)
        elif(split_method == 'char'): 
            char_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=450,
                chunk_overlap=50,
                length_function=len
            )
            splitted_docs= char_splitter.split_documents(documents)
        else: 
            raise ValueError() 
        
    def docToVector(self,embedding:str='OPENAI',model:str="text-embedding-ada-002",vectorStore:str="FAISS"):
        """_summary_

        Args:
            embedding (str, optional): _description_. Defaults to 'OPENAI'.
            model (str, optional): _description_. Defaults to "text-embedding-ada-002".

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        
        embeddings = None
        if(embedding == 'OPENAI'):
            embeddings = OpenAIEmbeddings(model=model,api_key = self.getOPENAI_API_KEY())
        elif(embedding == 'reserved for something else'):
            pass
        else:
            raise ValueError()
        if(self.splitted_docs == None):
            raise ValueError("Splitted_docs not loaded") 
        
        if(vectorStore == 'FAISS'):
            self.vectorStore = FAISS.from_documents(self.splitted_docs,embeddings)
        elif(vectorStore=='reserved'):
            pass
        else:
            raise ValueError("Invalid vectorStore value.")
        pass
    def setChat(self,chatName = 'ChatOpenAI',arg_dict=None):
        
        ai_dict = None
        if arg_dict == None:
            ai_dict = {
            "temperature": 0.5,
            "max_tokens": 2048,
            "model_name": "gpt-3.5-turbo"
        }
        else:
            ai_dict= arg_dict
            
        if(chatName == 'ChatOpenAI'):
            self.chat = ChatOpenAI(openai_api_key = self.getOPENAI_API_KEY(),
                                   temperature = ai_dict.get("temperature",0.5),
                                   max_tokens = ai_dict.get("max_tokens",2048),
                                   model_name = ai_dict.get("model_name","gpt-3.5-turbo"))
        else:
            raise ValueError("Invalid chatName value.")
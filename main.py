from time import sleep
from utils import APIKEY
from utils import PDFLoader


def main():


    qs = PDFQueryService()
    print(qs.getOPENAI_API_KEY())
    sleep(10)
    
    
    documents = PDFLoader("./data/Demain.pdf")
    sleep(10) 
    pass

class PDFQueryService:
    
    documents = None
    
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
    def getKeyObject(self):
        return self.key
    def getOPENAI_API_KEY(self):
        return self.key.getOPENAI_API_KEY() (self)
 
    def LoadDocuments(self,path:str,docType:str):
        if(docType == "pdf"):
            self.documents= PDFLoader(path)
        if(docType == "txt"):
            self.documents= TXTLoader(path) 

    
    
    
    
    
    
if __name__ == "__main__":
    main()

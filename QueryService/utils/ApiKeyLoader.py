
import os
from dotenv import load_dotenv






class APIKEY():

    OPENAI_API_KEY = None
    
    def __init__(cls):
        pass

    def setKeyFromEnv(self):
        load_dotenv()
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        
    
    def setOPENAI_API_KEY(self)->None:
        pass
    
    def getOPENAI_API_KEY(self)->str:
        if(self.OPENAI_API_KEY == None):
            self.setKeyFromEnv()    
        return self.OPENAI_API_KEY
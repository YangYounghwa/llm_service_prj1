from time import sleep

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

from langchain.vectorstores import FAISS

from CustomQueryModule import QueryEngine






def main():


    qs = QueryEngine()
    print(qs.getOPENAI_API_KEY())
    qs.LoadDocuments("data\Demian.pdf",docType="pdf")
    qs.docToVector()
    qs.setChat()
    qs.setChain()  
    
    qList = ["What does the Egg mean?", 
             "Who is the person that the protagonist is searching for?",
             "Meaning of the kiss?"]
    for q in qList:
        print("Query : ",q)
        result = qs.query(q)
        print(f'Result : {result["result"]}')
    



    
    
    
    
if __name__ == "__main__":
    main()

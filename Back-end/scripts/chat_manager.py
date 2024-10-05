from llm_manager import LLMManager
from langchain.memory import ConversationBufferMemory

from langchain.chains import LLMChain
class ChatManager(LLMManager):


    def __init__(self,queryRange,queryResolution):
        LLMManager.__init__(self,queryRange,queryResolution)   
        self.memory = ConversationBufferMemory(memory_key="chatHistory")          
    
    def __createChain__(self):
        prompt = self.promptGenerator.generate_prompt()
        memory = self.memory
        llm = self.model

        chain = LLMChain(
            llm = llm,
            memory = memory,
            prompt = prompt,
        )

        return chain
    
    def runChat(self):
        
        userInput = input("\n\n\n ______________________________________________________ \n\n")
        
        chain = self.__createChain__()
        
        while(userInput != "Exit"):
            
            print(chain.invoke(userInput = userInput))
            userInput = input("\n\n\n ______________________________________________________ \n\n")



newChat = ChatManager(20,20)
newChat.runChat()
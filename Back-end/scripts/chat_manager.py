from llm_manager import LLMManager
from langchain.memory import ConversationBufferMemory

from langchain.chains import LLMChain
class ChatManager(LLMManager):


    def __init__(self,queryRange,queryResolution):
        LLMManager.__init__(self,queryRange,queryResolution)   

    
    def __createChain__(self, template = None, question = None, answer = None):
        self.promptGenerator.generate_template(question = question, answer = answer)        
        return self.promptGenerator.update_chat_history(question = question, answer = answer)

    
        
    
    def runChat(self):
        
        
        userInput = None
        
        while(userInput != "Exit" or userInput == None):
            
            userInput = input("\n\n\n ______________________________________________________ \n\n")
            prompt = self.__createChain__(question = userInput)
            answer = self.model.invoke(prompt)         
            print(answer.content)
            prompt =  self.__createChain__(question = userInput,answer = answer.content)
            



newChat = ChatManager(20,20)
newChat.runChat()
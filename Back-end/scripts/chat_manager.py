from llm_manager import LLMManager
from langchain.memory import ConversationBufferMemory

from langchain.chains import LLMChain
class ChatManager(LLMManager):


    def __init__(self,queryRange,queryResolution):
        LLMManager.__init__(self,queryRange,queryResolution)   


    
    def __createChain__(self, template = None, question = None, answer = None):
        pass


    def runChat(self):
        
     
        userInput = None
        self.promptGenerator.generate_template()
        
        userInput = input("\n\n\n ______________________________________________________ \n\n")
        prompt = self.promptGenerator.update_chat_history(question = userInput)


        while(userInput != "Exit" or userInput == None):          
            answer = self.model.invoke(prompt)         
            print(answer.content)
            userInput = input("\n\n\n ______________________________________________________ \n\n")
            prompt = self.promptGenerator.update_chat_history(question = userInput, answer = answer.content)


newChat = ChatManager(20,20)
newChat.runChat()
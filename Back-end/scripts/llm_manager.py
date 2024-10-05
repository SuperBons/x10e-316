from langchain_openai import OpenAI
from prompt_generator import PromptGenerator
import getpass
import os


#enter OpenAi Api Key
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "Your KEY"


#Loader class to easily switch out models

class LLMManager(): 
    def __init__(self,dataRange,dataResolution):
        self.model = OpenAI()
        self.promptGenerator = PromptGenerator(dataRange,dataResolution)
    
    #Leaving implementation to subclasses. Different use cases require different chains
    def generate_Response(self):
        raise NotImplementedError()
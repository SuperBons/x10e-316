from langchain.prompts import ChatPromptTemplate,PromptTemplate,MessagesPlaceholder
from device_data_query import DeviceDataQuery
from create_health_summary import CreateHealthSummary
from langchain.schema import SystemMessage,HumanMessage,AIMessage


class PromptGenerator:
    
    deviceData: DeviceDataQuery #Object containg anamolies and user device data as two list[string] 
    healthSummary: CreateHealthSummary #Object creates JSON of user health records accesible as dict

    def __init__(self,dataRange,dataResolution):
        
        #Load in user device data and health summary
        self.history = []
        self.deviceData = DeviceDataQuery(dataRange, dataResolution) 
        self.healthSummary = CreateHealthSummary()

    
    def generate_template(self):

    
        template = ChatPromptTemplate([
            ("system", """You are a medical chatbot talking to a patient. If you are able give a possible diagnosis. Use the patient's health summary,lab abnormalities, and chat history 
                to answer their questions. Keep your responses within 3-4 sentences and address all patient questions."""),
            ("human", "Here is my health summary" + self.healthSummary.get_health_summary_as_string()),
            ("system", "And here are my lab abnormalities" + self.deviceData.get_Abnormalities_as_string()),
            MessagesPlaceholder(variable_name="history", optional=True),
            ("human", "{userInput}")
        ])
        self.template = template

    def update_chat_history(self, question, answer = None):
        template = self.template
        history = self.history

        if(answer != None):
            history.append(("ai", answer))
             
        if(history != None):
            prompt = template.invoke({
                "history" : history,
                "userInput": question
                
            })
        history.append(("human", question))
        self.history = history
        return prompt
        

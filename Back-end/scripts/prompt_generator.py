from langchain.prompts import PromptTemplate
from device_data_query import DeviceDataQuery
from create_health_summary import CreateHealthSummary


class PromptGenerator:
    
    deviceData: DeviceDataQuery #Object containg anamolies and user device data as two list[string] 
    healthSummary: CreateHealthSummary #Object creates JSON of user health records accesible as dict

    def __init__(self,dataRange,dataResolution):
        
        #Load in user device data and health summary

        self.deviceData = DeviceDataQuery(dataRange, dataResolution) 
        self.healthSummary = CreateHealthSummary()

    def generate_prompt(self,promptType = None):
        template =  """
        
        You are a medical chatbot talking to a patient. Use patients health summary and lab abnormalities to answer patients questions
        . Given the following patient details:
        
        {patientHealthSummary}

        and the given lab abnormalities

        {abnormalities}
        
        {chatHistory}
        "Hello Doctor" {userInput}
        
        Keep your answers within 3-4 sentences. Adress all patient questions. 
        
        """
        
        prompt = PromptTemplate(
        input_variables=["patientHealthSummary","abnormalities","userInput","chatHistory"],
        template=template
        )

        partial_prompt = prompt.partial(patientHealthSummary = self.healthSummary.get_Health_Summary(), abnormalities = self.deviceData.get_Abnormalities())
        return partial_prompt
       

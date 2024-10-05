import pandas as pd
import json
from pathlib import Path


class CreateHealthSummary():
    
    def __init__(self):
        #Include logic for accessing database and health records
        #Store data as a csv file

        dataPath = '../importedData/userHealthSummary.csv'
        json_file_path = '../importedData/healthSummary.json'  # Replace with your output file path
        
        try:
            df = pd.read_csv(dataPath)
            data_dict = df.to_dict(orient='records') 
            
            with open(json_file_path, 'w') as json_file:
                json.dump(data_dict, json_file, indent=4)
            self.summaryPath = json_file_path
        
        except FileNotFoundError as e:
            raise FileNotFoundError("Conversion failed!") from e    
                  
    def get_Health_Summary(self): 
        summaryPath = self.summaryPath
        return json.loads(Path(summaryPath).read_text())


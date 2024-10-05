import pandas as pd
import json
from pathlib import Path


class CreateHealthSummary():
    
    def __init__(self):
        #Include logic for accessing database and health records
        #Store data as a csv file

        self.dataPath = '../importedData/userHealthSummary.csv'
        json_file_path = '../importedData/healthSummary.json'  # Replace with your output file path
        
        try:
            df = pd.read_csv(self.dataPath)
            data_dict = df.to_dict(orient='records') 
            
            with open(json_file_path, 'w') as json_file:
                json.dump(data_dict, json_file, indent=4)
            self.summaryPath = json_file_path
        
        except FileNotFoundError as e:
            raise FileNotFoundError("Conversion failed!") from e    
                  
    def get_health_summary(self): 
        summaryPath = self.summaryPath
        return json.loads(Path(summaryPath).read_text())
    
    def get_health_summary_as_string(self): 
        # Load the CSV file
        file_path = self.dataPath
        health_summary_df = pd.read_csv(file_path)

        # Convert the dataframe to a string
        return health_summary_df.to_string(index=False)



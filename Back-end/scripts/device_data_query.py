
import csv
class DeviceDataQuery():
    

    #(int)Data Range: Range of data wanted to be observed
    #(int)Data Resolution: Specify how many data points to pull from within range
    def __init__(self,dataRange,dataQuery):
        #Include logic for accessing database and health records
        #Store data as a csv file
        self.dataPath = '../importedData/dataQuery_arthritis.csv'
    
    def get_Abnormalities(self):
        dataPath = self.dataPath
        anamolies = []        
        # Open both CSV files in read mode
        with open(dataPath, 'r') as csv_file1:
            reader1 = csv.reader(csv_file1)
            next(reader1)
            # Iterate over rows in both files simultaneously
            for row1 in reader1:
                
                recorded_value = float(row1[1])
                lower_limit = float(row1[2])
                upper_limit = float(row1[3])
                critical_low_limit = float(row1[4]) 
                critical_high_limit = float(row1[5])               

                #Determine if value is above or below healthy normal range
                
                if recorded_value > upper_limit:
                    if recorded_value >= critical_high_limit: healthyBounds = " is critically high at " 
                    else: healthyBounds = " is high at "

                    anamolies.append((row1[0],healthyBounds,row1[-1]))
                
                elif recorded_value <lower_limit:
                    if recorded_value <= critical_low_limit: healthyBounds = " is critically low at " 
                    else: healthyBounds = " is low at "
                    
                    anamolies.append((row1[0],healthyBounds,row1[-1]))

        return anamolies
    
    def get_Abnormalities_as_string(self):
        dataPath = self.dataPath
        anamolies = ""       
        # Open both CSV files in read mode
        with open(dataPath, 'r') as csv_file1:
            reader1 = csv.reader(csv_file1)
            next(reader1)
            # Iterate over rows in both files simultaneously
            for row1 in reader1:
                recorded_value = float(row1[1])
                lower_limit = float(row1[2])
                upper_limit = float(row1[3])
                critical_low_limit = float(row1[4]) 
                critical_high_limit = float(row1[5])               

                #Determine if value is above or below healthy normal range
                
                if recorded_value > upper_limit:
                    if recorded_value >= critical_high_limit: healthyBounds = " is critically high at " 
                    else: healthyBounds = " is high at "

                    anamolies += str(row1[0]) + healthyBounds + str(row1[-1])
                
                elif recorded_value <lower_limit:
                    if recorded_value <= critical_low_limit: healthyBounds = " is critically low at " 
                    else: healthyBounds = " is low at "
                    
                    anamolies += str(row1[0]) + healthyBounds + str(row1[-1])
        
        if(anamolies == ""): anamolies = "None Recorded"

        return anamolies
    
    def get_Raw_Data(self):
        dataPath = self.dataPath
        data = []
        
        # Open both CSV files in read mode
        with open(dataPath, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            # Iterate over rows in both files simultaneously
            for row1 in reader:
                
                data.append(row1)

        return data


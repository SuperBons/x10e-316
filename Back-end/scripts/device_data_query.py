
import csv
class DeviceDataQuery():
    

    #(int)Data Range: Range of data wanted to be observed
    #(int)Data Resolution: Specify how many data points to pull from within range
    def __init__(self,dataRange,dataQuery):
        #Include logic for accessing database and health records
        #Store data as a csv file
        self.dataPath = '../importedData/dataQuery.csv'
    
    def get_Abnormalities(self):
        dataPath = self.dataPath
        anamolies = []        
        # Open both CSV files in read mode
        with open(dataPath, 'r') as csv_file1:
            reader1 = csv.reader(csv_file1)
            next(reader1)
            # Iterate over rows in both files simultaneously
            for row1 in reader1:
                
                #Determine if value is above or below healthy normal range
                
                if row1[1] > row1[3]:
                    if row1[1] >= row1[5]: healthyBounds = "is critically high at" 
                    else: healthyBounds = "is high at"

                    anamolies.append((row1[0],healthyBounds,row1[-1]))
                elif row1[1] < row1[2]:
                    if row1[1] <= row1[4]: healthyBounds = "is critically low at" 
                    else: healthyBounds = "is low at"
                    
                    anamolies.append((row1[0],healthyBounds,row1[-1]))

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


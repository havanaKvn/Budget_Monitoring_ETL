from datetime import date
import pandas as pd
import glob

today = date.today()
''' ### Delivered
def extract_raw_transaction(file_path):

    stored_in = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/"
    # Open and read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Split the text by two or more consecutive newline characters
    # Each empty line is typically represented by '\n\n' in text files
    #### Extract Account Details
    chunks = text.split('\n\n') 

    for chunk in chunks:
        # Open a file in write mode
        file = open(stored_in + "Transactions_Extracted_" + str(today)+ ".csv", "w")
        # Write some text to the file
        file.write(chunk)
        # Close the file
       # file.close() 

def extract_account_details(file_path):
    stored_in = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/"
    # Open and read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Split the text by two or more consecutive newline characters
    # Each empty line is typically represented by '\n\n' in text files
    #### Extract Account Details
    chunks = text.split('\n\n') 

    i = 0
    for chunk in chunks:   
        if i < 1:
            file = open( stored_in + "Account_details_" + str(today) + ".csv", "w")
            # Write some text to the file
            file.write(chunk)
            # Close the file
            file.close() 
        i +=1
'''       
###Development in progress
def extract_raw_transaction(file_path,leng):

    stored_in = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/1_Bronze/"
    # Open and read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Split the text by two or more consecutive newline characters
    # Each empty line is typically represented by '\n\n' in text files
    chunks = text.split('\n\n') 
    
    for chunk in chunks:
        # Open a file in write mode
        file = open(stored_in + "Transactions_Extracted_" +str(leng)+"_"+ str(today)+ ".csv", "w")
        # Write some text to the file
        file.write(chunk)
        # Close the file
        file.close() 

def delet_Header():

    path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/1_Bronze/Transactions_Extracted_0_2024-11-03.csv'
    stored_in = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/1_Bronze/"
    
    with open(path, 'r') as file:
        text = file.read()

    # Split the text by two or more consecutive newline characters
    # Each empty line is typically represented by '\n\n' in text files
    chunks = text.split(')')
 
    for chunk in chunks:
    
        # Open a file in write mode
        file = open(stored_in + "Transactions_No_Header_"+ str(today)+ ".csv", "w")
        # Write some text to the file
        file.write(chunk)
        # Close the file
        file.close()
    
    print(1)     

def Combine_All_Files(path):

    # Read all CSV files in the folder
    all_files = glob.glob(path)

    # List to store DataFrames
    df_list = []
    leng = len(all_files)
    # Iterate over the list of files and read each one
    for file in all_files:
        leng = leng - 1
        extract_raw_transaction(file,leng)
       
        
        #df = pd.read_csv(file)
        #df_list.append(df)

    # Concatenate all DataFrames into one
    #combined_df = pd.concat(df_list, ignore_index=True)

        #print(leng)    

if __name__ == "__main__":
    # Provide the path to your text file
    #file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/Source/1_Bronze/0455501C0181728157083044.csv'
    #extract_raw_transaction(file_path)
    #extract_account_details(file_path)

    # Path to the folder containing CSV files
    #path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/1_Bronze/*.txt'
    #Combine_All_Files(path)

    delet_Header()

    print("Extract Succed on " + str(today))

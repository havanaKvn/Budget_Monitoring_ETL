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
        #file = open(stored_in + "Transactions_Raw_" +str(leng)+"_"+ str(today)+ ".csv", "w")
        file = open(stored_in + "Transactions_Raw_"+ str(leng)+ ".csv", "w")
        # Write some text to the file
        file.write(chunk)
        # Close the file
        file.close() 

def extract_raw_transaction_All_Files(path):
    # Read all CSV files in the folder
    all_files = glob.glob(path)

    # List to store DataFrames
    df_list = []
    leng = len(all_files)
    # Iterate over the list of files and read each one
    for file in all_files:
        leng = leng - 1
        extract_raw_transaction(file,leng)

def read_csv_with_encodings(file, encodings=['utf-8', 'latin1', 'iso-8859-1']): 
    for encoding in encodings: 
        try: return pd.read_csv(file, sep=';', encoding=encoding) 
        except UnicodeDecodeError: continue 
    raise ValueError("None of the specified encodings worked.")

def Combine_All_Files(path):
    stored_in = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/"
    # Read all CSV files in the folder
    all_files = glob.glob(path)

    # List to store DataFrames
    df_list = []
    leng = len(all_files)
    
    # Iterate over the list of files and read each one
    for file in all_files:
      #df = pd.read_csv(file,delimiter=';',encoding='iso-8859-1')
      df = read_csv_with_encodings(file)
   
      df_list.append(df)
   
    # Concatenate all DataFrames into one
    combined_df = pd.concat(df_list,ignore_index=True, axis=0)
    combined_df.columns = combined_df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    combined_df.drop_duplicates(inplace = True)
    combined_df.to_csv(stored_in + 'Transaction_Extracted_Combined.csv', sep=';', index=False)

if __name__ == "__main__":
    # Provide the path to your text file
    #file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/Source/1_Bronze/0455501C0181728157083044.csv'
    #extract_raw_transaction(file_path)
    #extract_account_details(file_path)

    # Path to the folder containing CSV files
    path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/Source/*.csv'
    extract_raw_transaction_All_Files(path)
    combine_Path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/1_Bronze/*.csv'
    Combine_All_Files(combine_Path)

    print("Extract Succed on " + str(today))

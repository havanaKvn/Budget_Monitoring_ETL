from datetime import date

today = date.today()

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
        file = open(stored_in + "Transactions_Extracted_Test" + str(today)+ ".txt", "w")
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

    file = open( stored_in + "Account_details_Test" + str(today) + ".txt", "w")
    
    for chunk in chunks:
        # Write some text to the file
        file.write(chunk)
        # Close the file
        file.close() 

if __name__ == "__main__":
    # Provide the path to your text file
    file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/1_Bronze/0455501C0181728157083044.csv'

    extract_raw_transaction(file_path)
    extract_account_details(file_path)
    
    print(today)

from datetime import date
import pandas as pd
import csv

today = date.today()


'''
# Drop rows with missing values
df.dropna(inplace=True)

# Drop unnecessary columns (replace 'column_name' with actual column names)
df.drop(columns=['column_name1', 'column_name2'], inplace=True)

# Rename columns (replace 'old_name' and 'new_name' with actual names)
df.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'}, inplace=True)

# Save the cleaned DataFrame back to a CSV file
df.to_csv('cleaned_file.csv', index=False)

print("Data cleaning complete. Cleaned file saved as 'cleaned_file.csv'.")

'''

def Fact_Transaction_Tab():
    print("test")

def Dim_Bill_Tab():
    print("test")

if __name__ == "__main__":

    # Provide the path to your text file   
    #file_path = "..\Data\2_Silver\Transactions_Extracted_" + str(today)+".txt"
    #file_path = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Transactions_Extracted_" + str(today)+".txt"
    file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Transactions_Extracted_2024-10-09.csv'
    
    #with open('Transactions_Extracted_2024-10-09.csv', 'r') as file:
        #text = file.read()

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path,delimiter=';',encoding='cp1252')

    print(df.head())
    
    print("Extract Succed on " + str(today))
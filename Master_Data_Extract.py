from datetime import date
import pandas as pd
import csv
import uuid

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
# Provide the path to your text file   
#file_path = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Transactions_Extracted_" + str(today)+".txt"
file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Transactions_Extracted_2024-10-09.csv'
#file_path = "..\Data\2_Silver\Transactions_Extracted_" + str(today)+".txt"
#with open('Transactions_Extracted_2024-10-09.csv', 'r') as file:
    #text = file.read()


def Fact_Transaction_Tab_Cleanning():
    print("test")
        # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path,delimiter=';',encoding='cp1252')
    #print(df.head())

    # Drop unnecessary columns (replace 'column_name' with actual column names)
    #Bill_Raw = df.drop(columns=['Date', 'Montant(EUROS)'], inplace=True)

    # Rename columns (replace 'old_name' and 'new_name' with actual names)
    df.rename(columns={'Libellï¿½': 'Libele_Achat', 'Montant(EUROS)': 'Montant'}, inplace=True)

    # Save the cleaned DataFrame back to a CSV file
    #df.to_csv('cleaned_file.csv', index=False)

    print(df)

    print("Data cleaning complete. Cleaned file saved as 'cleaned_file.csv'.")

def Bill_Category(x):
    if  'ACHAT CB' in x:
        return 'Expense'
    elif 'PRELEVEMENT' in x:
        return 'Subscription'
    else:
        return 'To_Define'

def Bill_Category_Code(x):
    if  'Expense' in x:
        return 666
    elif 'Subscription' in x:
        return 261
    else:
        return 111

def Dim_Bill_Tab_Cleanning():
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path, delimiter=';', encoding='cp1252')
    #print(df.head())

    # Drop unnecessary columns (replace 'column_name' with actual column names)
    df.drop(columns=['Date', 'Montant(EUROS)'], inplace=True)

    # Rename columns (replace 'old_name' and 'new_name' with actual names)
    df.rename(columns={'Libellï¿½': 'Bill_Label'}, inplace=True)

    #Create Unique Id with uuid() function
    #df['Id_Bill'] = [uuid.uuid4().hex for _ in range(len(df))]

    #Create Unique INT Id 
    df['Id_Bill'] = range(1, len(df) + 1)

    #Define Bill Category
    df['Bill_Category'] = df['Bill_Label'].apply(Bill_Category)

    #Define Bill Category
    df['Id_Bill_Category'] = df['Bill_Category'].apply(Bill_Category_Code) 
                           
    #test = df['Libele_Achat'].unique
    
    #Rearange Columns 
    new_order = ['Id_Bill', 'Bill_Label','Id_Bill_Category','Bill_Category']  
    df = df[new_order]

    print(df)

    # Save the cleaned DataFrame back to a CSV file
    df.to_csv('C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Dim_Bill_Detail.csv', sep=';', index=False)

if __name__ == "__main__":
    
    Dim_Bill_Tab_Cleanning()
    
    print("Extract Succed on " + str(today))









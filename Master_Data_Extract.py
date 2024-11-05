from datetime import date
import pandas as pd
import csv
import uuid
import datetime

today = date.today()

# Provide the path to your text file   
#file_path = "C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Transactions_Extracted_" + str(today)+".txt"
#file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Transactions_Extracted_2024-10-09.csv'
file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Transaction_Extracted_Combined.csv'
#file_path = "..\Data\2_Silver\Transactions_Extracted_" + str(today)+".txt"
#with open('Transactions_Extracted_2024-10-09.csv', 'r') as file:
    #text = file.read()

# To convert date format
def Extract_Long_Date(date_list):
    date_object = datetime.datetime.strptime(date_list, '%d/%m/%Y')
    #return date_object.strftime('%d/%B/%Y')
    return date_object.strftime('%m/%d/%Y')

def Convert_Amount_Format(Amount):
    new_value = Amount.replace(',', '.')
    return new_value

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
    
def Fact_Transaction_Explicite():   
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path,delimiter=';',encoding='cp1252')
    #print(df.head())

    # Rename columns (replace 'old_name' and 'new_name' with actual names)
    df.rename(columns={'Libelle': 'Bill_Label', 'Montant(EUROS)': 'Amount'}, inplace=True)
    
    #Create Unique INT Id 
    df['Id_Bill'] = range(1, len(df) + 1)
    
    #Define Bill Category
    df['Bill_Category'] = df['Bill_Label'].apply(Bill_Category)
    
    #Define Bill Category
    df['Id_Bill_Category'] = df['Bill_Category'].apply(Bill_Category_Code) 

    #Define Long Date
    df['Date_Formated'] = [Extract_Long_Date(date_) for date_ in df['Date']]

    #Format Amount
    df['Amount'] = [Convert_Amount_Format(Amount) for Amount in df['Amount']]
                           
    #test = df['Libele_Achat'].unique
    
    #Rearange Columns 
    new_order = ['Date','Date_Formated', 'Bill_Label','Amount','Id_Bill','Id_Bill_Category','Bill_Category']  
    df = df[new_order] 

    #print(df)

    # Save the cleaned DataFrame back to a CSV file
    df.to_csv('C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Fact_Transaction_Explicite.csv', sep=';', index=False)

    print("Data cleaning complete. Cleaned file saved as 'cleaned_file.csv'.")

def Fact_Transaction_Tab_Cleanning():
    
    file_path = 'C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/2_Silver/Fact_Transaction_Explicite.csv'
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path,delimiter=';',encoding='cp1252')
 
    # Drop unnecessary columns (replace 'column_name' with actual column names)
    df.drop(columns=['Date','Bill_Label', 'Bill_Category'], inplace=True)

    # Rename columns (replace 'old_name' and 'new_name' with actual names)
    df.rename(columns={'Date_Formated': 'Date'}, inplace=True)

    #Rearange Columns 
    new_order = ['Date','Id_Bill','Id_Bill_Category','Amount']  
    df = df[new_order]

    # Save the cleaned DataFrame back to a CSV file
    df.to_csv('C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/3_Gold/Fact_Transaction.csv', sep=';', index=False)

    #print(df)

def Dim_Bill_Tab_Cleanning():

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path, delimiter=';', encoding='cp1252')
    #print(df.head())

    # Drop unnecessary columns (replace 'column_name' with actual column names)
    df.drop(columns=['Date', 'Montant(EUROS)'], inplace=True)

    # Rename columns (replace 'old_name' and 'new_name' with actual names)
    df.rename(columns={'Libelle': 'Bill_Label'}, inplace=True)

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

    #print(df)

    # Save the cleaned DataFrame back to a CSV file
    df.to_csv('C:/Users/kevin/OneDrive/Bureau/Personal_Project/Budget_Monitoring/Data/3_Gold/Dim_Bill_Detail.csv', sep=';', index=False)

if __name__ == "__main__":
    
    Fact_Transaction_Explicite()
    Dim_Bill_Tab_Cleanning()
    Fact_Transaction_Tab_Cleanning()
    
    print("Extract Succed on " + str(today))









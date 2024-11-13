from tkinter import *
from tkinter import filedialog
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define budget categories and their keywords
categories = {
    'Groceries': ['kroger #6', 'publix', 'wal-mart'],
    'Utilities': ['utilities', 'gpc', 'water', 'comcast'],
    'Dining Out': ['dining', 'restaurant', 'food', 'meal','little caesars',
                   'mcdonalds','japanese','chick fil a','everyday','ramen','wood fired',
                  'DD','hibachi','coffee'],
    'Personal': ['amazon','target','etsy','paypal'],
    'Travel': ['HILTON','hotel','travel','hilton'],
    'Gas': ['fuel', 'gas','gold creek mark','murphy','qt'],
    'Entertainment': ['reg', 'movies', 'games', 'orchards'],
    'Healthcare': ['health', 'medical', 'pharmacy', 'insurance'],
    'Salary': ['adp'],
    'Insurance': ['state farm'],
    'Mortgage': ['newrez'],
    'Withdrawl from/to Savings': ['savings'],
    'Zelle': ['zelle'],
    'Education': ['postpartum']
}

# Function to categorize expenses
def categorize_expense(description):
    description_lower = description.lower()
    for category, keywords in categories.items():
        if any(keyword in description_lower for keyword in keywords):
            return category
    return 'Other'  # Default category if no match found

# Load expenses from CSV
#def load_expenses(filename):
#return pd.read_csv(filename)

def load_expenses():
    filepath = filedialog.askopenfilename()
    print(filepath)
    df = pd.read_csv(filepath)     
    
    df2 = pd.DataFrame(df, columns = ['Transaction Date','Transaction Amount','Transaction Description'])
    
    Date = df2["Transaction Date"]
    Amount = df2["Transaction Amount"]
    Description = df2["Transaction Description"]
    return df2


# Sort expenses into categories
def sort_expenses(expenses):
    expenses['Category'] = expenses['Transaction Description'].apply(categorize_expense)
    return expenses.groupby('Category')['Transaction Amount'].sum().reset_index()

# Main function
def main():
    # Load expenses
    #load_expenses()
    #expenses_file = 'expenses.csv'  # Replace with your CSV file path
    #expenses = load_expenses(expenses_file)
    expenses = load_expenses()
    
    # Sort expenses
    sorted_expenses = sort_expenses(expenses)
    
    # Display the sorted expenses
    print(sorted_expenses)
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.pie(sorted_expenses['Transaction Amount'], labels=sorted_expenses['Category'],
           autopct='%1.1f%%')
    plt.show()

if __name__ == "__main__":
    main()
    window = Tk()
    button = Button(text='open',command=load_expenses)
    window.mainloop()
    

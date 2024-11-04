import csv
from datetime import datetime
import os 

CSV_FILE = "budget.csv"

# Function to load data from CSV
def load_data():
    data = []
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"{CSV_FILE} not found, starting fresh.")
    return data

# Function to save income/expense data to CSV
def save_data(amount, category, is_income):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        date_str = datetime.now().strftime("%Y-%m-%d")
        writer.writerow([date_str, amount, category, "Income" if is_income else "Expense"])

# Function to calculate monthly savings
def calculate_savings(data):
    total_income = 0
    total_expense = 0

    current_month = datetime.now().strftime("%Y-%m")
    
    for row in data:
        date, amount, category, type_ = row
        amount = float(amount)
        if date.startswith(current_month):
            if type_ == "Income":
                total_income += amount
            elif type_ == "Expense":
                total_expense += amount

    return total_income - total_expense
def clearfile():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE,mode='w'):
            pass
            print("File cleared successfully")
    else:
        print("no such file exists")

# Function to display a menu for user interaction
def show_menu():
    print("\nBudget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Monthly Savings")
    print("4. Exit")
    print("5. To clear file content")
    

# Main function
def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter income category (e.g., salary, bonus): ")
            save_data(amount, category, is_income=True)
            print("Income added.")
        
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category (e.g., groceries, rent): ")
            save_data(amount, category, is_income=False)
            print("Expense added.")
        
        elif choice == "3":
            monthly_savings = calculate_savings(load_data())
            print(f"Your savings for this month: RS. {monthly_savings:.2f}")
        
        elif choice == "4":
            print("Exiting the program.")
            break
        elif choice == "5":
            clearfile()
             
                 
        else:
            print("Invalid option. Please select again.")


if __name__ == "__main__":
    main()
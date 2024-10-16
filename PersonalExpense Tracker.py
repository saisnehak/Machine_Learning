#   Description: Build an expense tracker that allows users to log expenses and categorize them (e.g., food, transport, etc.).
#   Key Topics:
#    Use **lists** to store the expense entries.
# Use **tuples** to handle immutable data like the expense name and amount.
#  Use **sets** to manage unique categories of expenses.
# Implement **dictionary comprehensions** to create summaries of expenses by category.
 


expenses_list = []


categories_set = set()

def expense_track(category, amount):
    
    expense = (category, amount)  # Tuple stores category and amount
    expenses_list.append(expense)  # Add the expense to the list
    categories_set.add(category)   # Add the category to the set for uniqueness
    print(f"Expense '{category}' of amount {amount} added successfully.")


TOTAL_EXPENSES = 5
i = 0

while i < TOTAL_EXPENSES:
    try:
        
        category = input("Enter an expense category (e.g., food, transport): ").strip()
        if not category:
            raise ValueError("Expense category cannot be empty.")
        
      
        amount_input = input("Enter the expense amount: ").strip()
        if not amount_input:
            raise ValueError("Expense amount cannot be empty.")
        amount = float(amount_input)
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        
        
        expense_track(category, amount)
        
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    i += 1


print("\nAll Expenses:")                             # Display all expenses
if not expenses_list:
    print("No expenses recorded.")
else:
    for idx, (category, amount) in enumerate(expenses_list, 1):
        print(f"  {idx}. Category: {category}, Amount: {amount}")


expense_summary = {
    category: sum(amount for cat, amount in expenses_list if cat == category)
    for category in categories_set
}

# Display expense summary
print("\nExpense Summary by Category:")
if not expense_summary:
    print("No expense summaries available.")
else:
    for category, total in expense_summary.items():
        print(f"  Category: {category}, Total Amount: {total}")
def check_balance():
  global balance
  print("Your current balance is:", balance)
def deposit(amount):
  global balance
  balance += amount
  print("Deposit successful. Your new balance is:", balance)
def withdraw(amount):
  global balance
  if amount > balance:
    print("Insufficient funds.")
  else:
    balance -= amount
    print("Withdrawal successful. Your new balance is:", balance)

balance = 0
while True:
  print("Welcome to Banking!")
  print("1. Check Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    check_balance()
  elif choice == 2:
    try:
        amount = float(input("Enter the amount to deposit: "))
        deposit(amount)
    except ValueError:
      print("Invalid Input")
  elif choice == 3:
    try:
        amount = float(input("Enter the amount to withdraw: "))
        withdraw(amount)
    except ValueError:
      print("Invalid input")
  elif choice == 4:
    print("Thank you for using the banking system!")
    break
  else:
    print("Invalid choice. Please try again.")
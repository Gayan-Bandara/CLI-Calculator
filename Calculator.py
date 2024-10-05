# Initialize an empty list to store the history of calculations
history_list = []

# Function to print the history of calculations
def history():
  # If there are previous calculations, print them
  if history_list:
    for line in history_list:
      print(line)
  # If the history is empty, inform the user
  else:
    print("No past calculations to show")

# Function to add two numbers
def add(a, b):
  return a + b

# Function to subtract the second number from the first
def subtract(a, b):
  return a - b

# Function to multiply two numbers
def multiply(a, b):
  return a * b

# Function to divide the first number by the second
# If division by zero is attempted, return 'None'
def divide(a, b):
  try:
    return a / b
  except:
    return 'None'

# Function to raise the first number to the power of the second number
def power(a, b):
  return a ** b

# Function to find the remainder when the first number is divided by the second
def remainder(a, b):
  return a % b

# Function to handle user's choice of operation
def select_op(choice):
  # If the user selects '#', terminate the program
  if (choice == '#'):
    return -1
  # If the user selects '$', reset the program
  elif (choice == '$'):
    return 0
  # If the user selects '?', display the history of calculations
  elif choice == '?':
    history()
  # If the user selects one of the arithmetic operations, prompt for input numbers
  elif (choice in ('+','-','*','/','^','%')):
    while (True):
      # Prompt the user for the first number and allow termination or reset
      num1s = str(input("Enter first number: "))
      print(num1s)
      if num1s.endswith('$'):
        return 0
      if num1s.endswith('#'):
        return -1
      
      # Try to convert the input to a float, repeat if invalid
      try:
        num1 = float(num1s)
        break
      except:
        print("Not a valid number, please enter again")
        continue
    
    while (True):
      # Prompt the user for the second number and allow termination or reset
      num2s = str(input("Enter second number: "))
      print(num2s)
      if num2s.endswith('$'):
        return 0
      if num2s.endswith('#'):
        return -1
      
      # Try to convert the input to a float, repeat if invalid
      try:
        num2 = float(num2s)
        break
      except:
        print("Not a valid number, please enter again")
        continue

    # Perform the selected operation and display the result
    if choice == '+':
      print(num1, "+", num2, "=", add(num1, num2))
      # Save the calculation to history
      record = str(num1) + " + " + str(num2) + " = " + str(add(num1, num2))
      history_list.append(record)
      
    elif choice == '-':
      print(num1, "-", num2, "=", subtract(num1, num2))
      record = str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2))
      history_list.append(record)
      
    elif choice == '*':
      print(num1, "*", num2, "=", multiply(num1, num2))
      record = str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2))
      history_list.append(record)
  
    elif choice == '/':
      # Handle division by zero case
      if divide(num1, num2) == 'None':
        print("float division by zero")
        
      print(num1, "/", num2, "=", divide(num1, num2))
      record = str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2))
      history_list.append(record)
      
    elif choice == '^':
      print(num1, "^", num2, "=", power(num1, num2))
      record = str(num1) + " ^ " + str(num2) + " = " + str(power(num1, num2))
      history_list.append(record)

    elif choice == '%':
      print(num1, "%", num2, "=", remainder(num1, num2))
      record = str(num1) + " % " + str(num2) + " = " + str(remainder(num1, num2))
      history_list.append(record)

    else:
      print("Something Went Wrong")
  # If an unrecognized operation is selected
  else:
    print("Unrecognized operation")

# Main loop to keep the program running and accepting user input
while True:
  # Display the available options to the user
  print("Select operation.")
  print("1. Add      : + ")
  print("2. Subtract : - ")
  print("3. Multiply : * ")
  print("4. Divide   : / ")
  print("5. Power    : ^ ")
  print("6. Remainder: % ")
  print("7. Terminate: # ")
  print("8. Reset    : $ ")
  print("8. History  : ? ")
  
  # Take input from the user for the operation they wish to perform
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  
  # If the user selects '#', terminate the program
  if(select_op(choice) == -1):
    print("Done. Terminating")
    exit()

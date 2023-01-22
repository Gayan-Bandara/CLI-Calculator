history_list = []

def history():
  if history_list:
    for line in history_list:
      print(line)
  else:
    print("No past calculations to show")


def add(a,b):
  return a+b
  
def subtract(a,b):
  return a-b
  
def multiply (a,b):
  return a*b

def divide(a,b):
  try:
    return a/b
  except:
    return 'None'
def power(a,b):
  return a**b

def remainder(a,b):
  return a%b

def select_op(choice):
  if (choice == '#'):
    return -1
  elif (choice == '$'):
      return 0
  elif choice == '?':
      history()
  elif (choice in ('+','-','*','/','^','%')):
    while (True):
      num1s = str(input("Enter first number: "))
      print(num1s)
      if num1s.endswith('$'):
        return 0
      if num1s.endswith('#'):
        return -1
        
      try:
        num1 = float(num1s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    while (True):
      num2s = str(input("Enter second number: "))
      print(num2s)
      if num2s.endswith('$'):
        return 0
      if num2s.endswith('#'):
        return -1
      try:  
        num2 = float(num2s)
        break
      except:
        print("Not a valid number,please enter again")
        continue

    if choice == '+':
      print(num1, "+", num2, "=", add(num1, num2))
      record = str(num1) + " + " + str(num2) + " = " + str(add(num1,num2))
      history_list.append(record)
      
    elif choice == '-':
      print(num1, "-", num2, "=", subtract(num1, num2))
      record = str(num1) + " - " + str(num2) + " = " + str(subtract(num1,num2))
      history_list.append(record)
      
  
    elif choice == '*':
      print(num1, "*", num2, "=", multiply(num1, num2))
      record = str(num1) + " * " + str(num2) + " = " + str(multiply(num1,num2))
      history_list.append(record)
  
    elif choice == '/':
      if divide(num1,num2) == 'None':
        print("float division by zero")
        
      print(num1, "/", num2, "=", divide(num1, num2))
      record = str(num1) + " / " + str(num2) + " = " + str(divide(num1,num2))
      history_list.append(record)
      
    elif choice == '^':
      print(num1, "^", num2, "=", power(num1, num2))
      record = str(num1) + " ^ " + str(num2) + " = " + str(power(num1,num2))
      history_list.append(record)

    elif choice == '%':
      print(num1, "%", num2, "=", remainder(num1, num2))
      record = str(num1) + " % " + str(num2) + " = " + str(remainder(num1,num2))
      history_list.append(record)

    else:
      print("Something Went Wrong")
  else:
    print("Unrecognized operation")
    
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  
  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
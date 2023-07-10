import time

# Prompt user for input
msg = input("Enter your message: ")

# Perform automation function
def automation(msg, count):
  for i in range(count):
    print("{}, {}/{}".format(msg, i + 1, count))
    time.sleep(1)

# Try and except error handling function
while True:
  try:
    count = int(input("Enter the number of times to repeat: "))
    if count < 1:
      print(
        "Error: Invalid input. Please enter a positive number for the count.")
    else:
      break
  except ValueError:
    print("Error: Invalid input. Please enter a number for the count. \n")

# Re-executing and while loop
re_execute = "Y"
while re_execute == "Y":
  automation(msg, count)
  print("Automation complete! \n")  #Automation message

  # Restarting prompt
  re_execute = input("Would you like to automate again? (Y/N): ").upper()

  # All Conditionals
  if re_execute == "N":
    print("Ok, thank you for using my automation program! :)")
    time.sleep(2)
  elif re_execute == "Y":
    msg = input("Enter your message: ")
    while True:
      try:
        count = int(input("Enter the number of times to repeat:" ))
        if count < 1:
          print("Error: Invalid input. Please enter a positive number for the count.")
        else:
          break
      except ValueError:
        print("Error: Invalid input. Please enter a number for the count.")
  else:
    print("Invalid, didn't choose Y or N")
    time.sleep(2)
    break
#ENJOY! :)

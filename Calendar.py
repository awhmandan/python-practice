"""Calendar - user can view, add, update, delete events"""

from time import strftime, sleep

NAME = "Dan"
calendar = {}

def welcome():
  print("Hello {}".format(NAME))
  print("Calendar opening...")
  sleep(1)
  print("Today is", strftime("%A, %d %b %Y"))
  print(strftime("%I:%M:%S"))
  sleep(1)
  print("What would you like to do? ")
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("A to add, U to update, V to view, D to delete, X to exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("Calendar empty")
      else:
        print(calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter update: ")
      calendar[date] = update
      print("Update successful")
      print(calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (DD/MM/YYYY): ")
      if len(date) > 10 or int(date[6:10]) < int(strftime("%Y")):
        print("Invalid date entered")
        try_again = input("Try again? Y/N: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print("Event successfully added")
    elif user_choice == "D":
      if len(calendar.keys()) > 1:
        print("Calendar empty")
      else:
        event = input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("Event deleted")
            print(calendar)
          else:
            print("Incorrect event specified")
    elif user_choice == "X":
      start = False
    else:
      print("Invalid input. Exiting...")
      start = False
            
start_calendar()
          
          
          
    
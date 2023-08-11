import os
  # author: luka
  # date: Jun 25, 2023
  # making responcesmore optimized and effeceint 
  # v1

responseYes = [
  "yes", "y", "yeah", "yup", "yep", "sure", "yea", "ya", 'ye', 'yee'
]
responseNo = ["no", "n", "nope", "nah", "maybe"]


def getUserInput(question, *options):
  # author: luka
  # date: Jun 25, 2023
  # making input optimized and effeceint 
  # v1
  while True:
    response = input(question + " ").lower()
    for index, option in enumerate(options):
      if (response in option):
        return index
    print("Please enter a valid option")


def clear():
  # author: luka
  # date: Jun 25, 2023
  # clearing screen 
  # v1
  os.system('cls' if os.name == 'nt' else 'clear')


def getUserInputNumber(question, min, max):
  # author: luka
  # date: Jun 25, 2023
  # numerical response 
  # v1
  while True:
    response = input(question)
    try:

      if response.lower() == "a":
        value = max
      else:
        value = int(response)
      if (value <= max) and (value >= min):
        return value
        break
      print('Please enter a number between {0} and {1}'.format(min, max))
    except:
      print('Please enter a NUMBER between {0} and {1}'.format(min, max))

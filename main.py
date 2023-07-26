import easy
import medium
import hard
import useful


# Functions go here...
def math_quiz_challenge():
  # author: luka
  # date: Jun 25, 2023
  # math quiz chanlange def
  # v3.31

  # Get user input for difficulty level and quiz length
  difficulty = useful.getUserInput(
    'Choose difficulty level (Easy, Medium, Hard)', ['easy', 'e'],
    ['medium', 'm'], ['hard', 'h'])

  while True:
    try:
      nof = int(input('how many question you want? '))
      if nof not in range(1, 28):
        print("enter a valid number between 1 and 28")
      else:
        break  # Break out of the while loop if valid input
    except ValueError:
      print("Invalid input. Please enter a valid number. ")

  print()

  match difficulty:
    case 0:
      easy.questions(nof)
    case 1:
      medium.questions(nof)
    case 2:
      hard.questions(nof)
    case _:
      print(
        'please enter a valid input')  # Use print instead of just the string


def statement_generator(statement, decoration):
  # author: luka
  # date: Jun 21, 2023
  # generates a border around prints
  # v1.1

  sides = decoration * 8

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""


def yes_no(question):
  # author: luka
  # date: Jun 21, 2023
  # user input if they want to chose yes or no
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "no"
      return response

    else:
      print("Please answer yes / no")


# Main routine goes here...

# greeting
# v1
statement_generator("Math Mastermind", "!")
print("  Welcome to the best math game")
print()

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
  print("instructions")

math_quiz_challenge()

statement_generator("congratulations!", "೫")


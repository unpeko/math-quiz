# Functions go here...
def math_quiz_challenge():
  # author: luka
  # date: Jun 24, 2023
  # math quiz chanlange def
  # v2

  # Get difficulty from difficulty index 
  from difficulty_mapping import difficulty_mapping

  # Get user input for difficulty level and quiz length
  difficulty = input("Choose difficulty level (Easy, Medium, Hard): ").lower()
  
  # Check if the difficulty level exists in the mapping
  if difficulty in difficulty_mapping:
      index = difficulty_mapping[difficulty]
      print(f"You chose difficulty level: {difficulty}. Index: {index}")
  else:
      print("Invalid difficulty level. Please choose from Easy, Medium, or Hard.")
  
  quiz_length = int(input("Enter the number of questions you want to answer: "))
  
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

import easy, medium, hard
import useful, psave
import fcntl, termios, struct
import os, sys


# Functions go here...
def terminal_size():
  # Author: luka
  # Date: aug 7, 2023
  # Witdh for centing prints and things
  # V1
  # Use struct and fcntl to fetch the terminal size (width and height)
  th, tw, hp, wp = struct.unpack(
    'HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))

  # Store the terminal width in the 'width' variable (assuming it's defined elsewhere in the code)
  global width
  width = tw

  # Return the terminal width and height
  return tw, th
terminal_size()


def stars():
  print("* *".center(width))


def leaderboard():
  # Author: luka
  # Date: aug 8, 2023
  # Leaderboard for players
  # V1.1
  leaderboard = psave.getleaderboard()
  print("~ LEADEROARD ~".center(width))
  stars()

  for i, player in enumerate(leaderboard):
    name = player["name"]
    score = player["score"]
    print(f"{i + 1}. {name}: {score}".center(width))
    # Lists players in decending order
  stars()


def math_quiz_challenge():
  # Author: luka
  # Date: Jun 25, 2023
  # Math quiz chanlange def
  # V3.31

  # Get user input for difficulty level and quiz length
  difficulty = useful.getUserInput(
    'Choose difficulty level (Easy, Medium, Hard)',
    ['easy', 'e'],
    ['medium', 'm'],
    ['hard', 'h'],
  )

  while True:
    # Ask user for how much quesions they want
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
  # Author: luka
  # Date: Jun 25, 2023
  # Math quiz chanlange def
  # V:2
    case 0:
      score = easy.questions(nof)
      # Links difficutly based on input
      player["score"] = player["score"] + score
      psave.saveplayer(player)
      # Adds players score form game so json file
    case 1:
      score = medium.questions(nof)
      player["score"] = player["score"] + score
      psave.saveplayer(player)
    case 2:
      score = hard.questions(nof)
      player["score"] = player["score"] + score
      psave.saveplayer(player)
    case _:
      # If user input not in case seiries, print this
      print('please enter a valid input')


def statement_generator(statement, decoration):
  # Author: luka
  # Date: Jun 21, 2023
  # Generates a border around prints
  # V1.1

  sides = decoration * 8

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom.center(width))
  print(statement.center(width))
  print(top_bottom.center(width))

  return ""


def yes_no(question):
  # Author: luka
  # Date: Jun 21, 2023
  # User input if they want to chose yes or no
  valid = False
  while not valid:
    # Put user in loop
    response = input(question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "no"
      return response

    else:
      print("Please answer yes / no")


def print_game_instructions():
  # Author: luka
  # Date: Jun 21, 2023
  # Game instructions
  # V2
  print("Welcome to the Math Quiz Game!\n")

  print(
    "In this thrilling and educational adventure, you will embark on a journey of mathematical challenges! "
    "Are you ready to put your math skills to the test and have a blast along the way? Strap in, because you "
    "are in for an exciting ride!/n")

  print(
    "At the beginning of the game, you will be presented with three exciting difficulty levels to choose "
    "from: Easy, Medium, and Hard. Each level comes with its own set of math questions that gradually "
    "increase in complexity. Whether you're a math whiz looking for a challenge or a beginner seeking to "
    "sharpen your skills, there's a difficulty level perfect for you!/n")

  print(
    "You will start with a total of three lives, so don't worry if you stumble along the way. Every correct "
    "answer will earn you points, and your ultimate goal is to score as high as you can. Remember, even if "
    "you lose a life, the game isn't over! Keep pushing yourself and see how far you can go./n"
  )

  print(
    "Once you've chosen a difficulty level, you'll have the chance to select the number of questions you wish "
    "to tackle. Prepare to face a series of brain-teasers that will test your arithmetic, algebraic, and even "
    "trigonometric abilities. But don't fret! We've got you covered with helpful hints if you ever find "
    "yourself in a tough spot./n")

  print(
    "As you progress through the game, each round will present a new question for you to solve. Read the "
    "questions carefully and take your time to calculate the answers. Remember, it's not just about speed; "
    "accuracy is key!/n")

  print(
    "Every correct answer will give you 1 score to add onto your final score, while an incorrect answer will cost"
    "you one of your precious lives. So stay focused, but most importantly, have fun! The thrill of solving a "
    "challenging math problem is truly rewarding./n")


def update_score_and_save(new_score):
  player["score"] = new_score
  psave.saveplayer(player)


# Main routine goes here...

# Greeting
# V2
statement_generator("Math Mastermind", "!")
print("Welcome to the best math game".center(width))
# Title screen
print()

name = input("what is your name? ")
# Author: luka
# Date: aug 10, 2023
# Ask user for name and save
# V1.3
# Load player form json
player = psave.loadplayer(name)

if (player == "not found"):
  player = psave.createplayer(name)
  # Creates player if not found in json
  instructions = yes_no("do you want instructions? ")
  # Author: luka
  # Date: aug 10, 2023
  # Ask user if they want instruction
  # V1.3
  if instructions == "yes":
    print_game_instructions()
    # If user inputs yes, print game instructions & break out of loop

  elif instructions == "no":
    print("have fun!")
    # If user inputs no, continue

  else:
    print("please enter either yes or no")
    # Continue loop if user inputs invalid option

else:
  # If user is found in json it will print this
  print(f"welcome back {name}")
  played_before = True

leaderboard()
# Displays leaderboard
print()

playing = True
while playing == True:
  # Put user in game loop
  math_quiz_challenge()
  # Starts math game
  print()

  # Congratulation  screen
  statement_generator("congratulations!", "೫")
  leaderboard()

  play_again = yes_no("Would you like to play again?")
  # Author: luka
  # Date: aug 8, 2023
  # Ask user if they want to play again
  # V1
  if play_again == "no":
    print("thank you for playing!")
    sys.exit
    # Exits program on user no input
  else:
    os.system('clear')
    leaderboard()
    # Repeats loop whist clearing screen

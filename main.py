import easy, medium, hard
import useful, psave
import fcntl, termios, struct
import os


# Functions go here...
def terminal_size():
  # author: luka
  # date: aug 7, 2023
  # witdh for centing prints and things
  # v1
  th, tw, hp, wp = struct.unpack(
    'HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0,
                                                           0)))
  global width
  width = tw
  return tw, th


terminal_size()


def stars():
  print("* *".center(width))


def leaderboard():
  # author: luka
  # date: aug 8, 2023
  # leaderboard for players
  # v1.1
  leaderboard = psave.getleaderboard()
  print("~ LEADEROARD ~".center(width))
  stars()

  for i, player in enumerate(leaderboard):
    name = player["name"]
    score = player["score"]
    print(f"{i + 1}. {name}: {score}".center(width))
  stars()


def math_quiz_challenge():
  # author: luka
  # date: Jun 25, 2023
  # math quiz chanlange def
  # v3.31

  # Get user input for difficulty level and quiz length
  difficulty = useful.getUserInput(
    'Choose difficulty level (Easy, Medium, Hard)',
    ['easy', 'e'],
    ['medium', 'm'],
    ['hard', 'h'],
  )

  while True:
    try:
      nof = int(input('how many question you want? '))
      if nof not in range(1, 30):
        print("enter a valid number between 1 and 28")
      else:
        break  # Break out of the while loop if valid input
    except ValueError:
      print("Invalid input. Please enter a valid number. ")

  print()

  match difficulty:
  #v:2
    case 0:
      score = easy.questions(nof)
      player["score"] = player["score"] + score
      psave.saveplayer(player)
    case 1:
      score = medium.questions(nof)
      player["score"] = player["score"] + score
      psave.saveplayer(player)
    case 2:
      score = hard.questions(nof)
      player["score"] = player["score"] + score
      psave.saveplayer(player)
    case _:
      print('please enter a valid input')


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


def print_game_instructions():
  print("Welcome to the Math Quiz Game!\n")

  print(
    "In this thrilling and educational adventure, you will embark on a journey of mathematical challenges! "
    "Are you ready to put your math skills to the test and have a blast along the way? Strap in, because you "
    "are in for an exciting ride!\n")

  print(
    "At the beginning of the game, you will be presented with three exciting difficulty levels to choose "
    "from: Easy, Medium, and Hard. Each level comes with its own set of math questions that gradually "
    "increase in complexity. Whether you're a math whiz looking for a challenge or a beginner seeking to "
    "sharpen your skills, there's a difficulty level perfect for you!\n")

  print(
    "You will start with a total of three lives, so don't worry if you stumble along the way. Every correct "
    "answer will earn you points, and your ultimate goal is to score as high as you can. Remember, even if "
    "you lose a life, the game isn't over! Keep pushing yourself and see how far you can go.\n"
  )

  print(
    "Once you've chosen a difficulty level, you'll have the chance to select the number of questions you wish "
    "to tackle. Prepare to face a series of brain-teasers that will test your arithmetic, algebraic, and even "
    "trigonometric abilities. But don't fret! We've got you covered with helpful hints if you ever find "
    "yourself in a tough spot.\n")

  print(
    "As you progress through the game, each round will present a new question for you to solve. Read the "
    "questions carefully and take your time to calculate the answers. Remember, it's not just about speed; "
    "accuracy is key!\n")

  print(
    "Every correct answer will give you 1 score to add onto your final score, while an incorrect answer will cost"
    "you one of your precious lives. So stay focused, but most importantly, have fun! The thrill of solving a "
    "challenging math problem is truly rewarding.\n")


def update_score_and_save(new_score):
  player["score"] = new_score
  psave.saveplayer(player)


# Main routine goes here...

# greeting
# v2
statement_generator("Math Mastermind", "!".center(width))
print("Welcome to the best math game".center(width))
print()

name = input("what is your name? ")
# author: luka
# date: Jun 21, 2023
# ask user for name and save
# v1.3
player = psave.loadplayer(name)

if (player == "not found"):
  player = psave.createplayer(name)
  played_before = yes_no("do you want instructions? ")
  # author: luka
  # date: Jun 21, 2023
  # ask user if played_before
  # v1.2
  if played_before == "yes":
    print_game_instructions()

  else:
    print("please enter either yes or no")

else:
  print(f"welcome back {name}")
  played_before = True

leaderboard()
print()

playing = True
while playing == True:
  math_quiz_challenge()
  print()

  statement_generator("congratulations!", "೫".center(width))
  leaderboard()
  play_again = yes_no("Would you like to play again?")
  # author: luka
  # date: aug 8, 2023
  # ask user if they want to play again
  # v1
  if play_again == "no":
    print("thank you for playing!")
    exit()
  else:
    os.system('clear')
    leaderboard()

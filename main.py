# Functions go here...


def statement_generator(statement, decoration):
  # author: luka
  # date: Jun 21, 2023
  # generates a border around prints
  # v1

  sides = decoration

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""


# Main routine goes here...

# greeting
# v1
statement_generator("Math Mastermind", "!")

import time


def slep1():
  time.sleep(3)


# Author: luka
# Date: Jun 25, 2023
# Easy questions and answers
# V1.6
def questions(NOQ):
  qus = [
    '1 + 1 = ',
    '1 + 2 = ',
    '2 + 2 = ',
    '2 + 3 = ',
    '3 + 3 = ',
    '3 + 4 = ',
    '4 + 4 = ',
    '4 + 5 = ',
    '5 + 5 = ',
    '5 + 6 = ',
    '6 + 6 = ',
    '6 + 7 = ',
    '7 + 7 = ',
    '7 + 8 = ',
    '8 + 8 = ',
    '8 + 9 = ',
    '9 + 9 = ',
    '10 + 10 = ',
    '10 + 11 = ',
    '11 + 11 = ',
    '11 + 12 = ',
    '12 + 12 = ',
    '12 + 13 = ',
    '13 + 13 = ',
    '13 + 14 = ',
    '14 + 14 = ',
    '14 + 15 = ',
    '15 + 15 = ',
    '15 + 16 = ',
  ]
  answer = [
    ['2'],
    ['3'],
    ['4'],
    ['5'],
    ['6'],
    ['7'],
    ['8'],
    ['9'],
    ['10'],
    ['11'],
    ['12'],
    ['13'],
    ['14'],
    ['15'],
    ['16'],
    ['17'],
    ['18'],
    ['20'],
    ['21'],
    ['22'],
    ['23'],
    ['24'],
    ['25'],
    ['26'],
    ['27'],
    ['28'],
    ['29'],
    ['30'],
    ['31'],
  ]
  help_msg = [
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another puppy enters the litter of puppy,\
    how many puppy would their now be?',
    'use addition, imagine you have 2 pigs and another pigs enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
    'use addition, imagine you have 2 pigs and another pig enters the litter of pigs,\
    how many pigs would their now be?',
  ]

  score = 0
  # Sets intial score at begining of game
  lives = 3
  # Sets intial lives
  # Author: luka
  # Date: aug 11, 2023
  # Dificulty processing
  # V1.5
  for i in range(NOQ):
    # For interger in quesion rage...
    output = input(qus[i]).lower()
    # Gets uesrs input for question, i equals the interger in the range
    if output in answer[i]:
      # If user input is corespondant to answer..A
      print('correct')
      print('lives:', lives)
      # Display current lives
      score += 1
      # Adds 1 score
      print('score:', score)
      # Print current socre
      print()

    else:
      # If user is not coesopnant to ansewr array...
      print('incorrect')
      print('answer:', str(answer[i][0]))
      # Print the right answer
      print('help:', help_msg[i])
      # Print help msg
      lives -= 1
      # Take away a life
      print('lives:', lives)
      # Print lives
      print('score:', score)
      # Print score
      print()

    if lives <= 0:
      # If lives is less than 0...
      print("you died")
      slep1()
      # Pauses program

      return score
      break
  return score

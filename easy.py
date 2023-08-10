import time
import os

def slep1():
  time.sleep(3)
  
# author: luka
# date: Jun 25, 2023
# easy questions and answers
# v1.6
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
    ['19'],
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
  lives = 3
  # author: luka
  # date: aug 11, 2023
  # diiificulty processing 
  # v1.5
  for i in range(NOQ):
    output = input(qus[i]).lower()
    if output in answer[i]:
      print('correct')
      print('lives:', lives)
      score += 1
      print('score:', score) 
      print()
      
    else:
      print('incorrect')
      print('answer:', str(answer[i][0]))
      print('help:', help_msg[i])
      lives -= 1
      print('lives:', lives)
      print('score:', score) 
      print()

    
    if lives <= 0:
      print("you died")
      slep1()

      return score 
      break 
  return score 

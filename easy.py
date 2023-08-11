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
  #sets intial score at begining of game
  lives = 3
  #sers intial lives
  # author: luka
  # date: aug 11, 2023
  # diiificulty processing 
  # v1.5
  for i in range(NOQ):
    #for interger in quesion rage...
    output = input(qus[i]).lower()
    #gets uesrs input for question
    if output in answer[i]:
      #if user input is corespondant to answer...
      print('correct')
      print('lives:', lives)
      #display current lives
      score += 1
      #adds 10 score
      print('score:', score) 
      #print current socre 
      print()
      
    else:
      #if user is not coesopnant to ansewr array...
      print('incorrect')
      print('answer:', str(answer[i][0]))
      #print the right answer 
      print('help:', help_msg[i])
      #print help msg
      lives -= 1
      #take away a life
      print('lives:', lives)
      #print lives
      print('score:', score) 
      #Print score
      print()

    
    if lives <= 0:
      #if lives is less than 0...
      print("you died")
      slep1()
      #pauses program

      return score
      break 
  return score 


# author: luka
# date: Jun 25, 2023
# easy questions and answers
# v1.2
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
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
  ]
  help_msg = [
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
    'use addition ',
  ]

  score = 0

  question = 0
  for i in range(0, NOQ):
    hidh = input(qus[question])
    if hidh == answer[question]:
      print('correct')
      score += 1
    else:
      print('incorrect')
      print('help:', help_msg[question])
      print('answer:', answer[question])

    question += 1

  print('your score:', score)

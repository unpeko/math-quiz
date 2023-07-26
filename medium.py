# author: luka
# date: Jun 25, 2023
# medium questions and answers
# v1.3
def questions(NOQ):
  qus = [
    '12 + 23',
    '34 - 16',
    '8 × 5',
    '45 ÷ 9',
    '5²',
    '√36',
    '3/4 + 1/4',
    '2/5 - 1/5',
    '1/3 × 9',
    '2/3 ÷ 2',
    '3 + 4 × 5',
    '(3 + 4) × 5',
    '2² + 3²',
    '9 - 5 ÷ 5',
    '5/8 of 64',
    '12 + 5 × 2 - 8',
    '2 × (4 + 6)',
    '3/4 of 20',
    '√144 + 2²',
    '5! (factorial)',
    '100 ÷ 10% (percentage)',
    '3² + √49',
    '8 - 2 + 5 × 3',
    '2 × (7 + 3) - 5',
    '25 ÷ 5 + 2³',
    '4 × 7 + 10 ÷ 2',
    '15 - 2² + √81',
    '7! ÷ 6!',
    '50% of 200',
    '2³ × 5 - 10',
  ]
  answer = [
    '35',
    '18',
    '40',
    '5',
    '25',
    '6',
    '1',
    '1/5',
    '3',
    '1/3',
    '23',
    '35',
    '13',
    '8',
    '40',
    '19',
    '20',
    '15',
    '14',
    '11',
    '120',
    '1000',
    '16',
    '20',
    '23',
    '13',
    '34',
    '5040',
    '25',
    '18',
    '5',
    '30',
  ]
  help_msg = ['get gud']

  score = 0

  lives = 3

  question = 0
  for i in range(0, NOQ):
    userAns = input(qus[question])
    if userAns == answer[question]:
      print('correct')
      score += 1
      print('lives:', lives)
      print()
    else:
      print('incorrect')
      print('help:', help_msg[question])
      print('answer:', answer[question])
      lives -= 1
      print('lives:', lives)
      print()
      if lives == 0:
        print("you died")
        exit()

    question += 1

  print('your score:', score)

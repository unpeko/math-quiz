  # author: luka
  # date: Jun 25, 2023
  # easy questions and answers
  # v1
def questions(NOQ):
  qus = [
  '1 + 1','1 + 2'
    
  ]
  answer = [
    '2','3'
  ]
  question = 0
  for i in range(0,NOQ): 
    hidh = input(qus[question])
    if hidh == answer[question]:
      print('correct')
    else:
      print('incorrect')
    question += 1
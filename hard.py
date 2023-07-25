  # author: luka
  # date: Jun 25, 2023
  # hard questions and answers
  # v1.1
def questions(NOQ):
  qus = [
    '√(16 + 9)',
    '2⁵',
    '6!',
    'log₂(64)',
    '3 + 4 × 5 ÷ 3 - 1',
    '3² + 4³',
    '√(144 + 25)',
    '(2 + 3)²',
    '3/4 + 4/5',
    '2/3 ÷ 3/4',
    'sin(30°)',
    'cos(45°)',
    'tan(60°)',
    'sin²(45°) + cos²(45°)',
    'log₅(125)',
    '5P2 (permutations)',
    '7C3 (combinations)',
    '√(36 × 49)',
    '2³ + 3⁴',
    'log₃(27)',
    'tan(45°) - sin(60°)',
    'cos²(30°) - sin²(30°)',
    '√(5² + 12²)',
    '√(10 + 2³)',
    '2^(1/2) × 4^(1/2)',
    '5! - 4!',
    'log₁₀(1000)',
    'tan(45°) × cos(60°)',
    'sin(45°) + cos(30°)',
    'sin(30°) × cos(60°)',
    '√(5 × 10 ÷ 2)',
    'log₂(16) + log₃(81)',
  ]
  answer = [
    '5',
    '32',
    '720',
    '6',
    '12',
    '91',
    '13',
    '25',
    '41/20',
    '8/9',
    '0.5',
    '√2/2',
    '√3',
    '1',
    '3',
    '20',
    '35',
    '84',
    '169',
    '3',
    '0.5',
    '0.75',
    '13',
    '√14',
    '√2',
    '20',
    '480',
    '3',
    '√3',
    '√2',
    '√5',
    '2',
    '3',
  ]
  question = 0
  for i in range(0,NOQ): 
    hidh = input(qus[question])
    if hidh == answer[question]:
      print('correct')
    else:
      print('incorrect')
    question += 1
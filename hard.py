import time


def slep1():
  # Author: luka
  # Date: Jun 30, 2023
  # Program pause
  # V1
  time.sleep(3)


# Author: luka
# Date: Jun 25, 2023
# Hard questions and answers
# V1.6
def questions(NOQ):
  qus = [
    '√(16 + 9) = ',  #1
    '2⁵ = ',  #2
    '6! = ',  #3
    'log₂(64) = ',  #4
    '3 + 4 × 5 ÷ 3 - 1(round to 3 decimal places) = ',
    '3² + 4³ = ',
    '√(144 + 25) = ',
    '(2 + 3)² = ',
    '3/4 + 4/5 = ',
    '2/3 ÷ 3/4 = ',
    'sin(30°) = ',
    'cos(45°) = ',
    'tan(60°) = ',
    'sin²(45°) + cos²(45°) = ',
    'log₅(125) = ',
    '5P2 (permutations) = ',
    '7C3 (combinations) = ',
    '√(36 × 49 = )',
    '2³ + 3⁴ = ',
    'log₃(27) = ',
    'tan(45°) - sin(60°) = ',
    'cos²(30°) - sin²(30°) = ',
    '√(5² + 12²) = ',
    '√(10 + 2³) = ',
    '2^(1/2) × 4^(1/2) = ',
    '5! - 4! = ',
    'log₁₀(1000) = ',
    'tan(45°) × cos(60°) = ',
    'sin(45°) + cos(30°) = ',
    'sin(30°) × cos(60°) = ',
    '√(5 × 10 ÷ 2) = ',
    'log₂(16) + log₃(81) = ',
  ]
  answer = [['5'], ['32'], ['720'], ['6'], ['8.666'], ['91'], ['13'], ['25'],
            ['31/20'], ['8/9'], ['0.5'], ['sqrt2/2'], ['sqrt3'], ['1'], ['3'],
            ['20'], ['35'], ['84'], ['169'], ['3'], ['0.5'], ['0.75'], ['13'],
            ['sqrt14'], ['sqrt2'], ['20'], ['480'], ['3'], ['sqrt3'],
            ['sqrt2'], ['sqrt5'], ['2'], ['3']]

  help_msg = [
    'To find the square root of a number, you need to find a number that,\
    when multiplied by itself, equals the given number. For example,\
    to find √(16 + 9), first calculate 16 + 9, and then find the square\
    root of the result.',
    'To find the power of a number, multiply the number by itself the\
    given number of times. For example, 2⁵ means 2 multiplied by itself\
    5 times: 2 * 2 * 2 * 2 * 2.',
    'Factorial means multiplying a number by all positive integers less\
    than it. For example, 6! means 6 * 5 * 4 * 3 * 2 * 1.',
    'To find the logarithm of a number to a given base, you need to find\
    the exponent to which the base must be raised to get the given number.\
    For example, log₂(64) means 2 raised to what power equals 64?',
    'Follow the order of operations: parentheses, exponents, multiplication\
    and division (from left to right), and finally addition and subtraction\
    (from left to right). For example, to solve 3 + 4 × 5 ÷ 3 - 1, perform\
    multiplication and division before addition and subtraction.',
    'To find the power of a number, multiply the number by itself the given\
    number of times. For example, 3² means 3 * 3, and 4³ means 4 * 4 * 4.',
    'To find the square root of a number, you need to find a number that,\
    when multiplied by itself, equals the given number. For example, to find\
    √(144 + 25), first calculate 144 + 25, and then find the square root of the result.',
    'To find the square of a sum, add the two numbers inside the parentheses\
    and then square the result. For example, (2 + 3)² means (2 + 3) * (2 + 3).',
    'To add or subtract fractions with different denominators, find a common\
    denominator and then perform the operation. For example, to solve 3/4 + 4/5,\
    find a common denominator and add the fractions.',
    'To divide fractions, multiply the first fraction by the reciprocal of the\
    second fraction. For example, to solve 2/3 ÷ 3/4, multiply 2/3 by 4/3.',
    'Use trigonometric functions to find the value of angles in a right triangle.\
    For example, sin(30°) is the ratio of the side opposite the angle to the hypotenuse.',
    'Use trigonometric functions to find the value of angles in a right triangle.\
    For example, cos(45°) is the ratio of the adjacent side to the hypotenuse.',
    'Use trigonometric functions to find the value of angles in a right triangle.\
    For example, tan(60°) is the ratio of the side opposite the angle to the adjacent side.',
    'The sum of the squares of the sine and cosine of an angle is always equal to 1.\
    For example, sin²(45°) + cos²(45°) equals 1.',
    'To find the logarithm of a number to a given base, you need to find the exponent\
    to which the base must be raised to get the given number. For example, log₅(125)\
    means 5 raised to what power equals 125?',
    'To find the number of permutations of selecting k items from a set of n items,\
    use the formula nPk = n! / (n - k)!. For example, 5P2 means 5 items selected 2\
    at a time, so 5P2 = 5! / (5 - 2)!',
    'To find the number of combinations of selecting k items from a set of n items,\
    use the formula nCk = n! / (k! * (n - k)!). For example, 7C3 means 7 items selected\
    3 at a time, so 7C3 = 7! / (3! * (7 - 3)!).',
    'To find the square root of a product, find the square root of each factor and then\
    multiply the results. For example, √(36 × 49) means √36 * √49.',
    'To find the power of a number, multiply the number by itself the given number of\
    times. For example, 2³ means 2 * 2 * 2, and 3⁴ means 3 * 3 * 3 * 3.',
    'To find the logarithm of a number to a given base, you need to find the exponent\
    to which the base must be raised to get the given number. For example, log₃(27)\
    means 3 raised to what power equals 27?',
    'Use trigonometric functions to find the value of angles in a right triangle. For\
    example, tan(45°) - sin(60°) means the tangent of 45° minus the sine of 60°.',
    'The trigonometric identity cos²θ - sin²θ = 1 can be used to simplify trigonometric\
    expressions. For example, cos²(30°) - sin²(30°) equals 1.',
    'To find the hypotenuse of a right triangle, use the Pythagorean Theorem: c² = a² + b²,\
    where c is the hypotenuse, and a and b are the other two sides. For example, √(5² + 12²)\
    means √(5 * 5 + 12 * 12).',
    'To find the square root of a sum, add the two numbers inside the parentheses and then\
    find the square root of the result. For example, √(10 + 2³) means √(10 + 8).',
    'To find the product of square roots, find the square root of each factor and then\
    multiply the results. For example, 2^(1/2) × 4^(1/2) means √2 * √4.',
    'To find the factorial of a number, multiply the number by all positive integers less\
    than it. For example, 5! means 5 * 4 * 3 * 2 * 1.',
    'To find the logarithm of a number to base 10, find the exponent to which 10 must be\
    raised to get the given number. For example, log₁₀(1000) means 10 raised to what power\
    equals 1000?',
    'Use trigonometric functions to find the value of angles in a right triangle. For example,\
    tan(45°) times cos(60°) means the tangent of 45° multiplied by the cosine of 60°.',
    'Use trigonometric functions to find the value of angles in a right triangle. For example\
    , sin(45°) plus cos(30°) means the sine of 45° added to the cosine of 30°.',
    'Use trigonometric functions to find the value of angles in a right triangle. For example,\
    sin(30°) times cos(60°) means the sine of 30° multiplied by the cosine of 60°.',
    'To find the square root of a product, find the square root of each factor and then multiply\
    the results. For example, √(5 × 10 ÷ 2) means √(5 * 10 / 2).',
    'To find the sum of logarithms with different bases, use the change of base formula: log_a(x)\
    = log_b(x) / log_b(a). For example, log₂(16) + log₃(81) means log(16) / log(2) + log(81) / log(3).',
  ]

  score = 0
  # Sets intial score at begining of game
  lives = 3
  # SeTs intial lives
  # Author: luka
  # Date: aug 11, 2023
  # Diiificulty processing
  # V1.5
  for i in range(NOQ):
    # For interger in quesion rage...
    output = input(qus[i]).lower()
    # Gets uesrs input for question
    if output in answer[i]:
      # If user input is corespondant to answer...
      print('correct')
      print('lives:', lives)
      # Display current lives
      score += 10
      # Adds 10 score
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

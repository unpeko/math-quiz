import time
import os

def slep1():
  time.sleep(3)
  
# author: luka
# date: Jun 25, 2023
# medium questions and answers
# v1.5
def questions(NOQ):
  qus = [
    '12 + 23 = ',
    '34 - 16 = ',
    '8 × 5 = ',
    '45 ÷ 9 = ',
    '5² = ',
    '√36 = ',
    '3/4 + 1/4 = ',
    '2/5 - 1/5 = ',
    '1/3 × 9 = ',
    '2/3 ÷ 2 = ',
    '3 + 4 × 5 = ',
    '(3 + 4) × 5 = ',
    '2² + 3² = ',
    '9 - 5 ÷ 5 = ',
    '5/8 of 64 = ',
    '12 + 5 × 2 - 8 = ',
    '2 × (4 + 6) = ',
    '3/4 of 20 = ',
    '√144 + 2² = ',
    '5! (factorial) = ',
    '100 ÷ 10% (percentage) = ',
    '3² + √49 = ',
    '8 - 2 + 5 × 3 = ',
    '2 × (7 + 3) - 5 = ',
    '25 ÷ 5 + 2³ = ',
    '4 × 7 + 10 ÷ 2 = ',
    '15 - 2² + √81 = ',
    '7! ÷ 6! = ',
    '50% of 200 = ',
    '2³ × 5 - 10 = ',
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
  help_msg = [
      'To add two numbers, simply add their digits. For example, 12 + 23 equals 35.',
      'To subtract one number from another, subtract their digits. For example, 34 - 16 equals 18.',
      'To multiply two numbers, multiply their digits. For example, 8 × 5 equals 40.',
      'To divide one number by another, divide their digits. For example, 45 ÷ 9 equals 5.',
      'To find the square of a number, multiply the number by itself. For example, 5² equals 25.',
      'To find the square root of a number, find a number that, when multiplied by \
      itself, equals the given number. For example, √36 equals 6.',
      'To add fractions with the same denominator, simply add their numerators. For \
      example, 3/4 + 1/4 equals 1.',
      'To subtract fractions with the same denominator, simply subtract their numerators.\
      For example, 2/5 - 1/5 equals 1/5.',
      'To multiply a whole number and a fraction, multiply the whole number by the numerator\
      of the fraction. For example, 1/3 × 9 equals 3.',
      'To divide a fraction by a whole number, divide the numerator of the fraction by the\
      whole number. For example, 2/3 ÷ 2 equals 1/3.',
      'To evaluate an expression with multiple operations, follow the order of operations:\
      parentheses, exponents, multiplication and division (from left to right), and finally \
      addition and subtraction (from left to right). For example, 3 + 4 × 5 equals 23.',
      'To evaluate an expression with parentheses, first calculate the value inside the parentheses.\
      For example, (3 + 4) × 5 equals 35.',
      'To find the sum of the squares of two numbers, square each number and then add the results.\
      For example, 2² + 3² equals 13.',
      'To evaluate an expression with multiple operations, follow the order of operations:\
      parentheses, exponents, multiplication and division (from left to right), and finally\
      addition and subtraction (from left to right). For example, 9 - 5 ÷ 5 equals 8.',
      'To find a percentage of a number, multiply the percentage by the number and divide by\
      100. For example, 5/8 of 64 equals 40.',
      'To evaluate an expression with multiple operations, follow the order of operations:\
      parentheses, exponents, multiplication and division (from left to right), and finally\
      addition and subtraction (from left to right). For example, 12 + 5 × 2 - 8 equals 19.',
      'To evaluate an expression with parentheses, first calculate the value inside the \
      parentheses. For example, 2 × (4 + 6) equals 20.',
      'To find a percentage of a number, multiply the percentage by the number and divide\
      by 100. For example, 3/4 of 20 equals 15.',
      'To find the sum of a square root and a squared number, find the square root of the\
      squared number and add the results. For example, √144 + 2² equals 14.',
      'To find the factorial of a number, multiply the number by all positive integers less\
      than it. For example, 5! equals 120.',
      'To find a percentage of a number, divide the percentage by 100 and multiply by the \
      number. For example, 100 ÷ 10% equals 10.',
      'To find the sum of a squared number and a square root, first find the square root of \
      the squared number and then add the results. For example, 3² + √49 equals 16.',
      'To evaluate an expression with multiple operations, follow the order of operations: \
      parentheses, exponents, multiplication and division (from left to right), and finally \
      addition and subtraction (from left to right). For example, 8 - 2 + 5 × 3 equals 19.',
      'To evaluate an expression with parentheses, first calculate the value inside the\
      parentheses. For example, 2 × (7 + 3) - 5 equals 15.',
      'To find the sum of a division and a power of a number, first calculate the power of\
      the number and then divide by the given number. For example, 25 ÷ 5 + 2³ equals 13.',
      'To find the sum of a multiplication and a division, first calculate the division and \
      then add the results. For example, 4 × 7 + 10 ÷ 2 equals 34.',
      'To find the sum of a subtraction, a squared number, and a square root, first find the\
      square of the squared number and then add the results. For example, 15 - 2² + √81 equals 35.',
      'To find the factorial of a number, multiply the number by all positive integers less \
      than it. For example, 7! equals 5040.',
      'To find a percentage of a number, divide the percentage by 100 and multiply by the number.\
      For example, 50% of 200 equals 100.',
      'To find the sum of a power of a number and a subtraction, first calculate the power of\
      the number and then subtract the given number. For example, 2³ × 5 - 10 equals 40.',
  ]
  score = 0
  lives = 3
  for i in range(0, NOQ):
    output = input(qus[i]).lower()
    if output in answer[i]:
      print('correct')
      score += 1
      print('lives:', lives)
      print('score:', score)
      print()
      
    else:
      print('incorrect')
      print('help:', help_msg[i])
      print('answer:', answer[i])
      lives -= 1
      print('lives:', lives)
      if lives >= 0:
        print("you died")
        slep1()
        os.system('clear')
        return score 
        break 
  return score 
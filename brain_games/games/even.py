import random

# Правила игры, которые выведутся при запуске
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(0, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer

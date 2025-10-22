import random

# Правила игры, которые выведутся при запуске
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def generate_round():
    """
    Генерирует вопрос и правильный ответ для одного раунда игры.
    Возвращает кортеж: (вопрос, правильный_ответ)
    """
    number = random.randint(0, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer

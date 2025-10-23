import random

RULES = "What number is missing in the progression?"


def make_progression(start, step, length):
    return [start + i * step for i in range(length)]


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(2, 10)
    length = random.randint(5, 10)

    progression = make_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, correct_answer

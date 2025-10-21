import prompt
import random

def welcome_user(): 
    """Приветствует пользователя и возвращает его имя"""
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name

def is_even_game(user_name):
    """Игра: проверка, чётное ли число"""
    count = 0
    while count < 3:
        num = random.randint(0, 999)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question: ' + str(num))
        inp = prompt.string('Your answer: ')

        correct_answer = 'yes' if num % 2 == 0 else 'no'

        if inp == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{inp}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")

def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    is_even_game(user_name)


import prompt


def run_game(game):
    """Запускает игру, используя её логику."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print(game.RULES)
    rounds_to_win = 3
    count = 0

    while count < rounds_to_win:
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')

        if answer == str(correct_answer):
            print("Correct!")
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    else:
        print(f"Congratulations, {name}!")

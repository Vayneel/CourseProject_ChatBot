"""
Games for chat_bot
rock-scissors-paper
guess-the-number
"""

import random
from stories import stories


def rsp() -> str:
    """
    Play rock-scissors-paper
    :return: amount of wins
    """

    points_rsp_start = 0
    points_rsp_end = 0

    try:
        rounds = int(input('Enter amount of rounds: '))
    except ValueError:
        return 'Error. Try to enter integer next time'

    signs = ('rock', 'scissors', 'paper')

    for _ in range(rounds):
        your_sign = input('Enter rock, scissors or paper: ').lower()
        rand_sign = signs[random.randint(0, 2)]

        if your_sign in signs:
            points_rsp_start += 1 if your_sign == 'rock' and rand_sign == 'scissors' else 0
            points_rsp_start += 1 if your_sign == 'scissors' and rand_sign == 'paper' else 0
            points_rsp_start += 1 if your_sign == 'paper' and rand_sign == 'rock' else 0
            print(f'My sign - {rand_sign}')
            print('Win!' if points_rsp_start != points_rsp_end else 'Loose.')
            points_rsp_end = points_rsp_start
        else:
            print('Incorrect sign.')

    return f'You won {points_rsp_start}\\{rounds} times'


def gtn() -> str:
    """
    Play guess-the-number
    :return: number of try
    """

    try:
        bot_edge = int(input('Enter bottom edge of numbers to guess: '))
        top_edge = int(input('Enter top edge of numbers to guess: '))
        amount_of_tries = int(input('Enter amount of tries, you want: '))
    except ValueError:
        return 'Error. Try to enter integer next time'

    number_to_guess = random.randint(bot_edge, top_edge)

    for number_of_try in range(amount_of_tries):
        try:
            your_guess = int(input('Try to guess number: '))
        except ValueError:
            print('Error. Try to enter integer next time')
            continue

        if your_guess == number_to_guess:
            return f'Correct! Number of tries - {number_of_try + 1}'

    return f'You loose, correct answer --> {number_to_guess}'


def grs() -> str:
    """
    Get some story
    :return: random story
    """

    return stories[random.randint(0, len(stories) - 1)]

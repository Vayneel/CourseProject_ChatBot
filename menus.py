"""
Menus containing functions
"""

from pyjokes import get_joke
from games_and_stories import rsp, gtn, grs
from art import tprint


def start_menu() -> bool or None:
    """
    Start menu
    :return: true or false
    """

    tprint('\nCHAT-BOT', font='small')

    match input('Hey! Want to talk?\n\t1.Yes!\n\t2.No\n(Enter number of answer)>>> '):
        case '1':
            print('Great!\n')
            return True

        case '2':
            print('I\'ll miss you. Bye.')
            return False
        case _:
            print('Seems, you\'ve entered incorrect answer. Restart program.')


def main_menu() -> str:
    """
    Main menu of chat_bot
    :return: your choose
    """
    main_choose = input("""What should I do?\n\t1.Recommend to me...\n\t2.Tell me...\n\t3.Let's play...
\t4.Stop talk (exit)!\n(Enter number of answer)>>> """)
    print()
    return main_choose


def recommend_film() -> None:
    """
    Recommend film by genre
    :return: Nothing
    """
    film_genre = input('Enter genre (comedy, fantasy, horror): ').lower()
    match film_genre:
        case 'comedy':
            print('Comedies: [Free Guy], [Deadpool], [Man From Toronto]\n')
        case 'fantasy':
            print('Fantasies: [Avatar], [Flash], [Shazam!]\n')
        case 'horror':
            print('Horrors: [30 Days Of Night], [The Void], [It]\n')
        case _:
            print('Seems, you\'ve entered something wrong.\n')
            recommend_menu()


def recommend_music() -> None:
    """
    Recommend music by genre
    :return: Nothing
    """
    music_genre = input('Enter genre (pop, classic, rock): ').lower()
    match music_genre:
        case 'pop':
            print('Pop music: [Call Me Maybe], [Bad Guy], [Get Lucky]\n')
        case 'classic':
            print(
                'Сlassic music: [Symphony №40 - Mozart], [Fidelio - Beethoven], [Motezuma - Vivaldi]\n')
        case 'rock':
            print('Rock music: [Smells Like Teen Spirit], [We Will Rock You], [Highway to Hell]\n')
        case _:
            print('Seems, you\'ve entered something wrong.\n')
            recommend_menu()


def recommend_game() -> None:
    """
    Recommend game by genre
    :return: Nothing
    """
    game_genre = input('Enter genre (rpg, slasher, horror): ').lower()
    match game_genre:
        case 'rpg':
            print('RPG games: [Horizon], [Witcher3], [TESV:Skyrim]\n')
        case 'slasher':
            print('Slasher games: [Devil May Cry], [NieR:Automata], [God Of War]\n')
        case 'horror':
            print('Horror games: [Resident Evil], [Dead Space], [Amnesia]\n')
        case _:
            print('Seems, you\'ve entered something wrong.\n')
            recommend_menu()


def recommend_menu() -> None:
    """
    Menu of recommend menu part
    :return:
    """

    recommend_choose = input("""What should I recommend?\n\t1.Film\n\t2.Music\n\t3.Game\n\t4.Return
(Enter number of answer)>>> """)

    print()
    match recommend_choose:
        case '1':
            recommend_film()
        case '2':
            recommend_music()
        case '3':
            recommend_game()
        case '4':
            return
        case _:
            print('Seems, you\'ve entered something wrong.\n')
            recommend_menu()


def play_menu() -> None:
    """
    Play game
    :return: Nothing
    """
    play_choose = input("""What you want to play?\n\t1.Rock-Scissors-Paper\n\t2.Guess-The-Number\n\t3.Return
(Enter number of answer)>>> """)

    print()
    match play_choose:
        case '1':
            print(rsp() + '\n')
        case '2':
            print(gtn() + '\n')
        case '3':
            return
        case _:
            print('Seems, you\'ve entered something wrong.\n')
            play_menu()


def tell_menu() -> None:
    """
    Tell about story or joke
    :return: Nothing
    """
    tell_choose = input("""What should I tell?\n\t1.Joke\n\t2.Interesting fact\n\t3.Return
(Enter number of answer)>>> """)

    print()
    match tell_choose:
        case '1':
            print(get_joke() + '\n')
        case '2':
            print(grs() + '\n')
        case '3':
            return
        case _:
            print('Seems, you\'ve entered something wrong.\n')
            tell_menu()

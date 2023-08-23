'''
Menus containing functions
'''

from pyjokes import get_joke
from games_and_stories import rsp, gtn, grs
from art import tprint
#from termcolor import cprint


def start_menu():
    '''
    Start menu
    :return: true or false
    '''

    tprint('\nCHAT-BOT', font='small')

    start_work = input('''Привіт! Бажаєш почати розмову?
\t1.Так!
\t2.Ні
(Введи цифру, як відповідь)>>> ''')

    match start_work:
        case '1':
            print('Круто!\n')
            return True

        case '2':
            print('Шкода. До зустрічі!')
            return False
        case _:
            print('Гадаю, ти помилився з відповіддю. Перезапусти програму!')


def main_menu():
    '''
    Main menu of chat_bot
    :return: your choose
    '''

    main_choose = input('''Що мені зробити?
\t1.Порекомендуй...
\t2.Розкажи...
\t3.Зіграймо в...
\t4.Досить розмовляти!
(Введи цифру, як відповідь)>>> ''')

    print()
    return main_choose


def recommend_film():
    '''
    Recommend film by genre
    :return: Nothing
    '''
    film_genre = input('Введи бажаний жанр (comedy, fantasy, horror): ').lower()
    match film_genre:
        case 'comedy':
            print('Серед найкращих комедій: [Free Guy], [Deadpool], [Man From Toronto]\n')
        case 'fantasy':
            print('Серед найкращих фентезі: [Avatar], [Flash], [Shazam!]\n')
        case 'horror':
            print('Серед найкращих фільмів-жахів: [30 Days Of Night], [The Void], [It]\n')
        case _:
            print('Схоже, ти ввів щось не те.\n')
            recommend_menu()


def recommend_music():
    '''
    Recommend music by genre
    :return: Nothing
    '''
    music_genre = input('Введи бажаний жанр (pop, classic, rock): ').lower()
    match music_genre:
        case 'pop':
            print('Серед найкращої поп-музики: [Call Me Maybe], [Bad Guy], [Get Lucky]\n')
        case 'classic':
            print(
                'Серед найкращих класичних мелодій: [Symphony №40 - Mozart], [Fidelio - Beethoven], [Motezuma - Vivaldi]\n')
        case 'rock':
            print('Серед найкращих рок пісень: [Smells Like Teen Spirit], [We Will Rock You], [Highway to Hell]\n')
        case _:
            print('Схоже, ти ввів щось не те.\n')
            recommend_menu()


def recommend_game():
    '''
    Recommend game by genre
    :return: Nothing
    '''
    game_genre = input('Введи бажаний жанр (rpg, slasher, horror): ').lower()
    match game_genre:
        case 'rpg':
            print('Серед найкращих рпг: [Horizon], [Witcher3], [TESV:Skyrim]\n')
        case 'slasher':
            print('Серед найкращих слешерів: [Devil May Cry], [NieR:Automata], [God Of War]\n')
        case 'horror':
            print('Серед найкращих хорорів: [Resident Evil], [Dead Space], [Amnesia]\n')
        case _:
            print('Схоже, ти ввів щось не те.\n')
            recommend_menu()


def recommend_menu():
    '''
    Menu of recomend menu part
    :return:
    '''

    recommend_choose = input('''Що тобі порекомендувати?
\t1.Фільм
\t2.Музику
\t3.Гру
\t4.Повернутись
(Введи цифру, як відповідь)>>> ''')

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
            print('Схоже, ти ввів щось не те.\n')
            recommend_menu()


def play_menu():
    '''
    Play game
    :return: Nothing
    '''
    play_choose = input('''В що ти хочеш зіграти?
\t1.Камінь-Ножиці-Папір
\t2.Вгадай число
\t3.Повернутись
(Введи цифру, як відповідь)>>> ''')

    print()
    match play_choose:
        case '1':
            print(rsp() + '\n')
        case '2':
            print(gtn() + '\n')
        case '3':
            return
        case _:
            print('Схоже, ти ввів щось не те.\n')
            play_menu()


def tell_menu():
    '''
    Tell about story or joke
    :return: Nothing
    '''
    tell_choose = input('''Що розповісти?
\t1.Жарт
\t2.Щось цікаве
\t3.Повернутись
(Введи цифру, як відповідь)>>> ''')

    print()
    match tell_choose:
        case '1':
            print(get_joke() + '\n')
        case '2':
            print(grs() + '\n')
        case '3':
            return
        case _:
            print('Схоже, ти ввів щось не те.\n')
            tell_menu()

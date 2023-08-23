'''
Console chat_bot for entertainment
'''

import menus as menu

start_cycle = menu.start_menu()

while start_cycle == True:
    match menu.main_menu():
        case '1':
            menu.recommend_menu()
        case '2':
            menu.tell_menu()
        case '3':
            menu.play_menu()
        case '4':
            break
        case _:
            print('Схоже, ти ввів щось не те.')

"""
Console chat_bot for entertainment
"""

import menus as menu

while 1:
    start_cycle = menu.start_menu()
    if start_cycle or not start_cycle:
        break

while start_cycle:
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
            print('Incorrect answer. Try again!')

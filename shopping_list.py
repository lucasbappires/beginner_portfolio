import os
import platform

shopping_list = []

def clear_terminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def show_list():
    for i, value in enumerate(shopping_list, start = 1):
        print(i, value)

print('Make your shopping list:')
while True:
    options = input('[a]dd [r]emove [l]ist [q]uit ').lower()

    if len(options) > 1:
        clear_terminal()
        print('Type only one letter that correspond to the given options.')
        continue
    elif not options.isalpha():
        clear_terminal()
        print('Don\'t type numbers or special characters.')
        continue

    if options == 'a':
        clear_terminal()
        item_to_add = input('What do you want to add to the list? ')
        shopping_list.append(item_to_add)
        clear_terminal()
        print('Item added!')
    elif options == 'r':
        if len(shopping_list) == 0:
            clear_terminal()
            print('Can\'t remove items from the list, as there is nothing to delete.')
            continue
        else:
            clear_terminal()
            print('Here\'s the list:')
            show_list()
            item_to_remove = input('What do you want to remove it? ')
            index = int(item_to_remove) - 1
            try:
                del shopping_list[index]
                clear_terminal()
                print('Item removed!')
            except IndexError:
                print('Couldn\'t find item with said value.')
                continue
            except ValueError:
                print('Type the value of the item you want to remove from the list.')
                continue
            except Exception:
                print('Undefined error.')
                continue
    elif options == 'l':
        if len(shopping_list) == 0:
            clear_terminal()
            print('Unable to list you the items, as there are no items on the list.')
            continue
        else:
            clear_terminal()
            show_list()
    elif options == 'q':
        clear_terminal()
        sair = input('Are you sure you want to quit? (y/n) ')
        if sair != 'y':
            continue
        else:
            clear_terminal()
            print('Have a nice day!')
            break
    else:
        clear_terminal()
        print('Type a valid input!')
        continue
from colorama import init
from colorama import Fore, Back, Style
init()


# ввод числа
def data_in() -> str: 
    return input(Back.MAGENTA + Fore.RED + 'Введите рациональное число: ')


# ввод оператора
def data_op() -> str: 
    return input(Back.YELLOW + 'Введите оператор: ')


def print_result(data):
    
    print(f'{Fore.BLUE}{Back.GREEN}{data}')
    print(Style.RESET_ALL)

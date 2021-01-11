import os

BAD_RETURN_CODE = 'SOMETHING IS WRONG HERE...'
EMPTY_ERROR = "I PITY THE FOOL THAT HAS NO SCORE!"
NOTHING_ERROR = "You Tried And Still Failed"


def Screen_cleaner():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
import os

BAD_RETURN_CODE = 'SOMETHING IS WRONG HERE...'
NOTHING_ERROR = "Nothing here!"


def Screen_cleaner():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
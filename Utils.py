import os

SCORES_FILE_NAME = 'score.txt'
BAD_RETURN_CODE = 'Something went wrong...'


def Screen_cleaner():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
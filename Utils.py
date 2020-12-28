import os

SCORES_FILE_NAME = 'score.txt'
BAD_RETURN_CODE = 'Something went wrong...'
FILE_NOT_FOUND = "File not found!"
FILE_EMPTY_ERROR = "Nothing in here to see!"


def Screen_cleaner():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def get_score_from_file(file_path):
    try:
        f = open(SCORES_FILE_NAME, 'r')
        score = f.readline()
        return score
    except:
        print("File Cannot Be Found")
    finally:
        f.close()
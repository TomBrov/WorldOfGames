import os

SCORES_FILE_NAME = 'score.txt'
BAD_RETURN_CODE = 'SOMETHING IS WRONG HERE...'
FILE_NOT_FOUND = "FILE NOT FOUND!"
FILE_EMPTY_ERROR = "I PITY THE FOOL THAT HAS AN EMPTY FILE!"


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
from flask import Flask, request
from Utils import *
from os import path

app = Flask(__name__)


@app.route('/', methods=['GET'])
def score_server():
    if path.exists(SCORES_FILE_NAME):
        current_score = get_score_from_file(SCORES_FILE_NAME)
        if current_score != '':
            return html_valid(current_score)
        else:
            return html_error(FILE_EMPTY_ERROR)
    else:
        return html_error(FILE_NOT_FOUND)


def html_valid(scores):
    return f'<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is <div id="score">{scores}</div></h1> </body> </html>'


def html_error(error):
    return f'<html> <head> <title>Scores Game</title> </head> <body> <body> <h1><div id="score" style="color:red">{error}</div></h1> </body> </html>'


if __name__ == '__main__':
    app.run(debug=True)
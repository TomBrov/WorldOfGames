from flask import Flask
from Utils import *
from redis import Redis

app = Flask(__name__)


def html_valid(scores):
    return f'<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is <div id="score">{scores}</div></h1></body> </html>'


def html_error(error):
    return f'<html> <head> <title>Scores Game</title> </head> <body> <body> <h1><div id="score" style="color:red">{error}</div></h1> </body> </html>'


@app.route('/', methods=['GET'])
def score_server():
    redis = Redis(host='redis',password='wog123', decode_responses=True)
    score = redis.get('user')
    score = int(score)

    if score is None:
        return html_error(NOTHING_ERROR)
    else:
        return html_valid(score)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8777)
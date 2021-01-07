FROM python:3-alpine
WORKDIR app
ADD MainScores.py /app
ADD Scores.txt /app
ADD CurrencyRouletteGame.py /app
ADD Game.py /app
ADD GuessGame.py /app
ADD Live.py /app
ADD MainGame.py /app
ADD MemoryGame.py /app
ADD Utils.py /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
RUN chmod -R 777 ./
EXPOSE 8777
CMD ["python", "MainScores.py"]
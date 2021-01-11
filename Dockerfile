FROM python:3-alpine
WORKDIR app
ADD MainScores.py /app
ADD Utils.py /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
RUN chmod -R 777 ./
EXPOSE 8777
CMD ["python", "MainScores.py"]
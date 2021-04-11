FROM python:3-alpine
WORKDIR app
ADD ./Dockerimage/* /app
RUN pip install -r requirements.txt
RUN chmod -R 777 ./
EXPOSE 8777
CMD ["python", "MainScores.py"]
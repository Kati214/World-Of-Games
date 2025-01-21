FROM python:latest
WORKDIR /app
COPY . /app
COPY Scores.txt /Scores.txt
RUN pip install -r requirements.txt
EXPOSE 8777
CMD ["python", "MainScores.py"]
FROM takeokunn/kaggle-gpu:latest

ENV APP_PATH /workspace
RUN mkdir $APP_PATH
WORKDIR $APP_PATH

COPY . .

FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

# do stuff here
RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install

COPY ["predict.py", "./"]

CMD ["pipenv", "run", "python", "predict.py", "2023", "5"]
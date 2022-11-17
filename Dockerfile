FROM python:3.9 as builder

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update 
RUN pip install --upgrade pip

COPY . .

COPY ./req.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r req.txt


FROM python:3.9

RUN mkdir -p /app



ENV APP_HOME=/app
WORKDIR $APP_HOME


COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/req.txt .
RUN pip install --no-cache /wheels/*


COPY . $APP_HOME

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
# FastAPI scrap + async selenium


### how to run app

###### from root directory

    docker-compose up --build

### migrations
    docker exec web alembic revision --autogenerate -m 'migration_1'
    docker exec web alembic upgrade head

### scrap

    docker exec -it web bash
    python src/scrap/loop_urls_generator.py
    python src/scrap/loop_items_generator.py
    python src/scrap/consumer_database.py


### FastAPI

###### app must be runing on `localhost:8000`


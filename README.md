# FastAPI scrap + async selenium

### migrations
    docker exec web alembic revision --autogenerate -m 'migration_1'
    docker exec web alembic upgrade head

### scrap

    docker exec web python src/scrap/selenium_links_publisher.py
    docker exec web python src/scrap/selenium_links_consumer.py

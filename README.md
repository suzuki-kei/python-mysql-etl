# python-mysql-etl

## 起動

    docker-compose up -d

## MySQL コンテナに接続する

    docker-compose exec mysql bash -c 'mysql -u$MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE'

## Python コンテナに接続する

    docker-compose run python bash
    pip install -r requirements.txt
    python src/main/python/main.py
    PYTHONPATH=src/main/python python src/test/python/utilities/language_test.py


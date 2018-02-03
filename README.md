# python-mysql-etl

## 起動

    docker-compose up -d

## MySQL に接続する

    docker-compose exec mysql mysql -uroot
    docker-compose exec mysql mysql -uproduct-user product
    docker-compose exec mysql mysql -umarketing-user marketing

## アプリケーションを実行する

    docker-compose run app python src/main/python/main.py

## テストを実行する

    docker-compose run app python -m unittest discover -s src/test/python -t .


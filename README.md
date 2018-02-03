# python-mysql-etl

## 起動

    docker-compose up -d

## MySQL コンテナに接続する

    docker-compose exec mysql bash -c 'mysql -u$MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE'

## アプリケーションを実行する

    docker-compose run app python src/main/python/main.py

## テストを実行する

    docker-compose run app python src/test/python/utilities/language_test.py


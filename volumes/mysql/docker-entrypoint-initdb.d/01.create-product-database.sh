#
# 商品データベースを作成する.
#

cat <<EOS | "${mysql[@]}"

CREATE DATABASE IF NOT EXISTS product;
CREATE USER 'product-user'@'%' IDENTIFIED BY '';
GRANT ALL ON product.* TO 'product-user'@'%' WITH GRANT OPTION;
USE product;

--
-- 商品カテゴリ.
--
CREATE TABLE product_categories
(
    -- ID.
    id INTEGER PRIMARY KEY AUTO_INCREMENT,

    -- 商品カテゴリコード.
    code VARCHAR(255) NOT NULL UNIQUE,

    -- 商品カテゴリ名.
    name VARCHAR(255) NOT NULL UNIQUE,

    -- 登録日時.
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 更新日時.
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 楽観的排他処理に用いるバージョン.
    version INTEGER NOT NULL DEFAULT 0
);

--
-- 商品.
--
CREATE TABLE products
(
    -- ID.
    id INTEGER PRIMARY KEY AUTO_INCREMENT,

    -- 商品名.
    name VARCHAR(255) NOT NULL UNIQUE,

    -- 登録日時.
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 更新日時.
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 楽観的排他処理に用いるバージョン.
    version INTEGER NOT NULL DEFAULT 0
);

EOS


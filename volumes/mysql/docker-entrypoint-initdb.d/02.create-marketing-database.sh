#
# マーケティングデータベースを作成する.
#
cat <<EOS | "${mysql[@]}"

CREATE DATABASE IF NOT EXISTS marketing;
CREATE USER 'marketing-user'@'%' IDENTIFIED BY '';
GRANT ALL ON marketing.* TO 'marketing-user'@'%' WITH GRANT OPTION;
USE marketing;

--
-- 顧客.
--
CREATE TABLE customers
(
    -- ID.
    id INTEGER PRIMARY KEY AUTO_INCREMENT,

    -- 顧客名.
    name VARCHAR(255) NOT NULL UNIQUE,

    -- メールアドレス.
    email VARCHAR(255) NOT NULL,

    -- 誕生日.
    birthday DATE NOT NULL,

    -- 登録日時.
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 更新日時.
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 楽観的排他処理に用いるバージョン.
    version INTEGER NOT NULL DEFAULT 0
);

--
-- 顧客プロフィール.
--
CREATE TABLE customer_profiles
(
    -- ID.
    id INTEGER PRIMARY KEY AUTO_INCREMENT,

    -- ニックネーム.
    nick_name VARCHAR(255) NOT NULL,

    -- 趣味.
    favorites TEXT NOT NULL,

    -- 自己紹介.
    self_introduction TEXT NOT NULL,

    -- 登録日時.
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 更新日時.
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- 楽観的排他処理に用いるバージョン.
    version INTEGER NOT NULL DEFAULT 0
);

EOS


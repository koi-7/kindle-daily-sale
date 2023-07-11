# kindle-daily-sale

Kindle の日替わりセールを Slack で通知する

# Usage

## ダウンロード

``` bash
$ cd ~
$ git clone https://github.com/koi-7/kindle-daily-sale.git
```

## `config.ini` ファイルの設定

`config/sample.ini` を参考に `config/config.ini` を記述する

## Requirements

``` bash
$ cd ~/kindle-daily-sale/
$ pip3 install -r requirements.txt
```

## ディレクトリの移動

`/opt/` 配下に設置する

``` bash
$ cd ~
$ sudo mv kindle-daily-sale/ /opt/
```

## cron の設定

毎朝 6 時に実行されるように設定する

``` bash
CRON_TZ=Asia/Tokyo

PYTHONPATH=$PYTHONPATH:/opt/kindle-daily-sale/
0 6 * * * /usr/bin/python3 -m kindle-daily-sale
```

タイムゾーンを反映するために cron を再起動する

``` bash
$ sudo systemctl restart cron
```

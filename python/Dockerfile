FROM python:3.11-slim

# 音声出力を使用するために必要なパッケージをインストール
RUN apt-get update && apt-get install -y alsa-utils curl cron

# 作業ディレクトリの設定（compose.ymlのworking_dirとも揃える）
WORKDIR /app

# requirements.txtのみを先にコピーして依存パッケージをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# .pyファイル群はcompose側のvolumesでマウントされるためCOPY不要

# CMDはcompose.ymlでcommand指定する場合は不要．main.pyを起動したい場合は下記
# CMD ["python", "main.py"]

CMD bash /app/test/test.sh

# crontab設定ファイルをコンテナにコピー
COPY crontab.txt /etc/cron.d/my-cron

# CMDでtest.sh→cronを順に実行
CMD bash /app/test/test.sh && cron -f

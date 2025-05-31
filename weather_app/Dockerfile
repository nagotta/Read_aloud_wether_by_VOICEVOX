FROM python:3.11-slim

# 音声出力を使用するために必要なパッケージをインストール
RUN apt-get update && apt-get install -y alsa-utils curl cron

# 作業ディレクトリの設定（compose.ymlのworking_dirとも揃える）
WORKDIR /app

# requirements.txtのみを先にコピーして依存パッケージをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# crontab設定ファイルをコンテナにコピー
COPY crontab.txt /etc/cron.d/my-cron

# 音声再生テスト，キャラクターと天気を予報する地域を設定，定期実行の開始
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]

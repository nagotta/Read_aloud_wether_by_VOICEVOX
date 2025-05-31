#!/bin/bash
#
# 音声再生テスト，キャラクターと天気を予報する地域を設定，定期実行の開始
#

set -e

# .envファイルから環境変数を読み込む
set -a
source /app/.env
set +a

# 1. 音声ファイルテスト
bash /app/aplay.sh -t

# 2. 設定ファイルがなければセットアップ案内
if [ ! -f "$CONFIG_FILE" ]; then
    echo "設定ファイル（$CONFIG_FILE）が見つかりません"
    echo "別のターミナルで↓を実行してセットアップしてください"
    echo "docker compose run --rm python python3 /app/config.py"
    echo "セットアップ完了後、pythonコンテナを再起動してください"
    cron -f    # ここで止めて「サービス維持」
    exit 0
fi

# 3. main.py → 再生 → cron
python3 /app/main.py
bash /app/aplay.sh
cron -f

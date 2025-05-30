#!/bin/bash

set -e # エラーが発生した場合、スクリプトを終了する

# .envの変数を環境変数として読み込む
set -a
source .env
set +a

# testディレクトリの絶対パスを取得
TEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


# 各ファイルのパスを変数定義
TEXT_FILE="${TEST_DIR}/test_text.txt"
QUERY_FILE="${TEST_DIR}/test_query.json"
AUDIO_FILE="${TEST_DIR}/test_audio.wav"

# テキストファイル作成
echo -n "こんにちは、音声合成の世界へようこそ" > "$TEXT_FILE"

# HOST_IPとHOST_PORTを使ってリクエストを投げる
curl -s \
    -X POST \
    "${HOST_IP}:${HOST_PORT}/audio_query?speaker=1" \
    --get --data-urlencode text@"$TEXT_FILE" \
    > "$QUERY_FILE"

curl -s \
    -H "Content-Type: application/json" \
    -X POST \
    -d @"$QUERY_FILE" \
    "${HOST_IP}:${HOST_PORT}/synthesis?speaker=1" \
    > "$AUDIO_FILE"

# 音声ファイルのテスト再生
aplay "$AUDIO_FILE" || echo "音声ファイルの再生に失敗しました。"
#!/bin/bash
# VOICEVOX APIで音声ファイルを生成し再生するスクリプト
# -t オプション時はテスト音声、それ以外は天気テキスト

set -e

# .envファイルから環境変数を読み込む
load_env() {
  set -a
  source /app/.env
  set +a
}

# VOICEVOXエンドポイントURLをセット
set_voicevox_url() {
  VOICEVOX_URL="http://${VOICEVOX_HOSTNAME}:${VOICEVOX_CONTAINER_PORT}"
}

# VOICEVOX APIで音声ファイルを生成
# $1: 入力テキストファイル
# $2: 出力音声ファイル
# $3: 一時query.jsonパス
# $4: speaker_id（デフォルト1）
create_voicevox_audio() {
  local text_file="$1"
  local audio_file="$2"
  local query_file="$3"
  local speaker_id="${4:-1}"

  curl -s \
    -X POST \
    "${VOICEVOX_URL}/audio_query?speaker=${speaker_id}" \
    --get --data-urlencode text@"${text_file}" \
    > "${query_file}"

  curl -s \
    -H "Content-Type: application/json" \
    -X POST \
    -d @"${query_file}" \
    "${VOICEVOX_URL}/synthesis?speaker=${speaker_id}" \
    > "${audio_file}"
}

# aplayで音声再生
play_audio() {
  aplay "$1" || echo "音声ファイルの再生に失敗しました。"
}

# ----------------------------------------
# メイン処理
# ----------------------------------------

echo "音声再生のテストを開始"
load_env
set_voicevox_url

MODE="weather"  # デフォルトは天気予報

while getopts "t" opt; do
  case $opt in
    t) MODE="test" ;;  # テストモード
    *) ;;  # 他のオプションは無視
  esac
done

if [ "$MODE" = "test" ]; then
  # テスト音声用ファイル設定
  DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  TEXT_FILE="${DIR}/test_text.txt"
  QUERY_FILE="${DIR}/test_query.json"
  AUDIO_FILE="${DIR}/test_audio.wav"
  echo -n "こんにちは、音声合成の世界へようこそ" > "$TEXT_FILE"
else
  # 天気予報用ファイル設定
  AUDIO_FILE="/app/weather.wav"
  TEXT_FILE="/app/weather.txt"
  QUERY_FILE="/app/weather_query.json"
fi

create_voicevox_audio "$TEXT_FILE" "$AUDIO_FILE" "$QUERY_FILE" 1
play_audio "$AUDIO_FILE"

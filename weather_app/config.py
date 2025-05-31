#
# 設定ファイルや環境変数の読み込み、VOICEVOX話者・気象庁エリア一覧取得、CLIによるユーザ選択、設定保存/読込を行う
#
import os
import json
import requests

# .envファイルを読み込んで環境変数をdictとして返す
def load_env(env_path='.env'):
    env = {}
    if not os.path.exists(env_path):
        print(f".envファイルが見つかりません: {env_path}")
        return env
    with open(env_path) as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                env[k] = v
    return env

# .envからCONFIG_FILEのパスを取得（なければuser_config.jsonを使う）
def get_config_file_path(env):
    return env.get('CONFIG_FILE', 'user_config.json')

# VOICEVOXエンジンAPIから話者IDと名前の一覧を取得
def get_voicevox_speakers(env):
    host = env.get('VOICEVOX_HOSTNAME', 'voicevox-server')
    port = env.get('VOICEVOX_CONTAINER_PORT', '50021')
    url = f"http://{host}:{port}/speakers"
    try:
        res = requests.get(url)
        speakers = res.json()
        speaker_list = []
        for s in speakers:
            for style in s['styles']:
                speaker_list.append({
                    'id': style['id'],
                    'name': f"{s['name']}（{style['name']}）"
                })
        return speaker_list
    except Exception as e:
        print(f"VOICEVOXサーバーに接続できません: {e}")
        return []

# 気象庁エリア一覧（都道府県コードと名称）をJSONで取得
def get_weather_areas():
    area_url = "https://www.jma.go.jp/bosai/common/const/area.json"
    try:
        res = requests.get(area_url)
        offices = res.json().get('offices', {})
        return [{'code': code, 'name': info['name']} for code, info in offices.items()]
    except Exception as e:
        print(f"エリア一覧の取得に失敗: {e}")
        return []

# ユーザに検索ワードで絞り込み・番号選択させて1件選択
def search_and_select(options, display_field='name', example='例'):
    # ユーザに検索ワードで絞り込み・番号選択させて1件選択する
    while True:
        query = input(f"検索ワードを入力してください (e.g. {example}): ")
        matches = [(i, v) for i, v in enumerate(options) if query in v[display_field]]
        if not matches:
            print("該当がありません。もう一度入力してください。")
            continue
        for idx, item in matches:
            print(f"{idx}: {item[display_field]}")
        try:
            select = int(input("番号を選択: "))
            if any(idx == select for idx, _ in matches):
                return options[select]
        except Exception:
            pass
        print("正しい番号を入力してください。")

# 地域コード・キャラクターIDを設定ファイルに保存
def save_config(area_code, character_id, env):
    config_file = get_config_file_path(env)
    config = {'area_code': area_code, 'character_id': character_id}
    with open(config_file, 'w') as f:
        json.dump(config, f)

# 設定ファイルから保存済みの地域・キャラクター設定を読み込む
def load_config(env):
    config_file = get_config_file_path(env)
    if not os.path.exists(config_file):
        return None
    with open(config_file) as f:
        return json.load(f)

# ユーザにCLIで地域・キャラクターを選択させて設定・保存
def setup_config():
    env = load_env()
    print("【天気予報の地域を選択】")
    area_list = get_weather_areas()
    selected_area = search_and_select(area_list, display_field='name', example='香川')
    print(f"選択: {selected_area['name']}（コード: {selected_area['code']}）\n")
    
    print("【VOICEVOXキャラクターを選択】")
    speaker_list = get_voicevox_speakers(env)
    selected_speaker = search_and_select(speaker_list, display_field='name', example='ずんだもん')
    print(f"選択: {selected_speaker['name']}（ID: {selected_speaker['id']}）\n")
    
    save_config(selected_area['code'], selected_speaker['id'], env)
    print(f"設定を保存しました：{get_config_file_path(env)}")

# モジュール単体実行時に設定ウィザードを実行
if __name__ == '__main__':
    setup_config()

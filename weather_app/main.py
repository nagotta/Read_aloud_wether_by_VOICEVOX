#
# CLI設定ファイルと天気予報APIを利用し、天気テキストファイルを生成する
#
import os
from config import load_env, load_config
from weather import get_weather

def main():
    # .envと設定ファイルを読み込む
    env = load_env()
    config = load_config(env)
    if not config:
        print("設定ファイルがありません。まず設定ウィザードを実行してください。")
        return

    area_code = config['area_code']
    # 必要に応じて地点コード（観測所ID）なども設定ファイルに持たせてもOK

    # 天気予報情報を取得
    latest_temp, latest_precipitation10m, tommorow_weather, overview_forecast_text = get_weather(area=area_code, detail_area=area_code)

    # 書き出すテキスト内容を組み立て
    weather_text = "\n".join([
        latest_temp,
        latest_precipitation10m,
        tommorow_weather,
        overview_forecast_text
    ])

    # 出力先テキストファイルパス（例：.envに WEATHER_TEXT_PATH で指定可）
    output_path = env.get('WEATHER_TEXT_PATH', 'weather.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(weather_text)
    print(f"[INFO] 天気情報を{output_path}に出力しました。")

if __name__ == "__main__":
    main()

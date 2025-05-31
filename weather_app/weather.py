#
# 天気予報情報を気象庁APIから取得して、文章を生成する
#
import requests
from datetime import datetime

# 品質情報を確認し、データを文字列で返す
def confirm_aqc(data: list) -> str:
    if data[1] == 0:
        return str(data[0])
    else:
        return "品質情報を確認して下さい"

# 対象エリアデータのインデックスを返す
def find_index(data: list, code: str) -> int:
    return [num for num, i in enumerate(data) if i["area"]["code"] == code][0]

# 指定エリアの最新天気情報を取得して返す
def get_weather(area="370000", detail_area="370000", stnid="72086"):
    latest_time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
    latest_time_req = requests.get(latest_time_url)
    latest_datetime = datetime.strptime(latest_time_req.text, "%Y-%m-%dT%H:%M:%S%z")
    yyyymmdd = latest_datetime.strftime('%Y%m%d')
    h3 = ("0" + str((latest_datetime.hour//3)*3))[-2:]

    # 概況
    overview_forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area}.json"
    overview_forecast_req = requests.get(overview_forecast_url)
    overview_forecast_data = overview_forecast_req.json()
    overview_forecast_text = "\n".join(overview_forecast_data["text"].split())

    # 天気予報
    forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area}.json"
    forecast_req = requests.get(forecast_url)
    forecast_data = forecast_req.json()
    forecast_data = forecast_data[0]["timeSeries"][0]["areas"]
    forecast_data_target_index = find_index(forecast_data, detail_area)
    weathers = forecast_data[forecast_data_target_index]["weathers"]
    tommorow_weather = " ".join(weathers[1].split())

    # アメダス
    amedas_url = f"https://www.jma.go.jp/bosai/amedas/data/point/{stnid}/{yyyymmdd}_{h3}.json"
    amedas_req = requests.get(amedas_url)
    amedas_data = amedas_req.json()
    latest_key = max(amedas_data)
    latest_temp = confirm_aqc(amedas_data[latest_key]["temp"])
    latest_precipitation10m = confirm_aqc(amedas_data[latest_key]["precipitation10m"])

    latest_temp = f"現在の気温は{latest_temp} 度．"
    latest_precipitation10m = f"現在の降水量は10分あたり{latest_precipitation10m} ミリメートルです．"
    tommorow_weather = f"翌日の天気は{tommorow_weather}模様です．"
    overview_forecast_text = f"今日と明日の天気概況は，{overview_forecast_text}"
    return latest_temp, latest_precipitation10m, tommorow_weather, overview_forecast_text

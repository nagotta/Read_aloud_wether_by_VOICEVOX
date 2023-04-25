from get_wether_info import get_weater_infomation
import subprocess
import random
import os

def get_text():
    os.chdir("/home/kbit/make_vo")
    # nameidによって誰のボイスにするが決まる
    nameid = random.randint(0,19)
    f=open('id.txt', 'w')
    f.write(str(nameid))
    f.close()
    if nameid == 0 or nameid == 2 or nameid == 4 or nameid == 6:
        name = 'しこくめたん'
    elif nameid == 1 or nameid == 3 or nameid == 5 or nameid == 7:
        name = 'ずんだもん'
    elif nameid == 8:
        name = 'かすかべつむぎ'
    elif nameid == 10:
        name = 'はれうはう'
    elif nameid == 9:
        name = 'なみねりつ'
    elif nameid == 11:
        name = 'くろのたけひろ'
    elif nameid == 12:
        name = 'しらかみこたろう'
    elif nameid == 13:
        name = 'あおやまりゅうせい'
    elif nameid == 14:
        name = 'めいめいひまり'
    else:
        name = 'きゅうしゅうそら'

    # お天気情報を取得して変数に格納
    prologue = f'{name}が天気予報をお伝えします。'
    latest_temp = ''
    latest_precipitation10m = ''
    tommorow_weather = ''
    overview_forecast_text = ''
    epilogue = f'以上、{name}が天気予報をお伝えしました。'
    latest_temp, latest_precipitation10m, tommorow_weather, overview_forecast_text = get_weater_infomation.get_weather()
    text_list = [prologue, latest_temp, latest_precipitation10m, tommorow_weather, overview_forecast_text, epilogue]
    
    os.chdir("../voicevox_core-0.11.4/example/python")
    for text, num in zip(text_list, range(6)):
        
        # run.pyに値を渡して実行
        subprocess.call(['python','run.py','--text', text, '--speaker_id', str(nameid), '--root_dir_path', '../../release', '--num', str(num) ])
	
get_text()

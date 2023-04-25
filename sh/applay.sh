#!/bin/bash

# nameid読み込み
nameid=$(cat /home/kbit/make_vo/id.txt)
# nameid=$(grep -o '*' id.txt)
echo $nameid

# ディレクトリ移動
cd /home/kbit/voicevox_core-0.11.4/example/python/vo

# 音声ファイル再生
for i in {0..5}
do
    aplay $i-$nameid.wav
done

rm /home/kbit/voicevox_core-0.11.4/example/python/vo/*.wav
rm /home/kbit/make_vo/id.txt

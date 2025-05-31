# VOICEVOXキャラによる天気予報お知らせシステム

本システムはLinux系OS上で動作する天気予報音声通知システムです．設定時刻になると，ずんだもんや春日部つむぎ等の[VOICEVOX](https://voicevox.hiroshiba.jp/product/zundamon/)キャラクターが気温・降水量・気候状況を音声で知らせてくれます．

![お天気ずんだもん](https://github.com/nagotta/Read_aloud_wether_by_VOICEVOX/assets/86472676/9afd77a1-d191-4a83-af65-35a34f885509)

<!--## サンプルボイス ずんだもん-->
## サンプルボイス
- ずんだもん(ノーマル)
<!-- ここにwavを挿入 -->


## 構築手順
- 起動
```
$ git clone 
$ cd 
$ docker compose up -d

# 以下は初回起動時，またはキャラクター・地域変更時のみ実行(インタラクティブに設定)
$ docker compose run --rm python python3 /app/config.py
【天気予報の地域を選択】
検索ワードを入力してください (e.g. 香川): 香川
43: 香川県
番号を選択: 43
選択: 香川県（コード: 370000）

【VOICEVOXキャラクターを選択】
検索ワードを入力してください (e.g. ずんだもん): ずんだ
6: ずんだもん（ノーマル）
7: ずんだもん（あまあま）
8: ずんだもん（ツンツン）
9: ずんだもん（セクシー）
10: ずんだもん（ささやき）
11: ずんだもん（ヒソヒソ）
12: ずんだもん（ヘロヘロ）
13: ずんだもん（なみだめ）
番号を選択: 6
選択: ずんだもん（ノーマル）（ID: 3）

設定を保存しました：user_config.json

# コンテナの再起動を実施
$ docker compose restart python
```
- 停止
```
docker compose down
```

### ツールバージョン

- Docker version 27.4.1
- Ubuntu 24.04.1 LTS
- VOICEVOX ENGINE 0.23.0

## 参考サイト

[VOICEVOX GitHub](https://github.com/VOICEVOX)
[VOICEVOX_ENGINE](https://github.com/VOICEVOX/voicevox_engine/releases)
[【Colab / Python】気象庁API - 気象データの収集](https://qiita.com/T_Ryota/items/ef96d6575404a0fd46dd)

# VOICEVOXキャラによる天気予報お知らせシステム

VOICEVOXキャラ([ずんだもん、春日部つむぎ達](https://voicevox.hiroshiba.jp/product/zundamon/)が天気予報をお知らせしてくれるシステムを作成しました。

キャラを限定したい場合は[キャラを限定したい場合](#キャラを限定したい場合)を参考に必要な箇所を編集してください。

VOICEVOX COREをインストールしてvoフォルダ作成

main.pyを実行するには
VOICEVOX/.../python/run.pyを一部編集する必要があります。当リポジトリ内のrun.pyを参考に記述して下さい。
また、同ディレクトリ内にvoフォルダ(wavファイル入れ)を作成してください。

## ディレクトリ構成

<img width="403" alt="image" src="https://user-images.githubusercontent.com/86472676/234162796-1600576e-f8f1-4241-85f4-004b367b6db0.png">

## バージョン

* VOICEVOX CORE 0.11.4
/* ## サンプルボイス ずんだもん */

### キャラを限定したい場合

./make_vo/main.pyの13行目～32行目のifを任意のキャラクターのみコメントアウトしてください。

### 参考サイト

[天気予報取得コード](https://qiita.com/T_Ryota/items/ef96d6575404a0fd46dd#%E7%9B%AE%E6%AC%A1)

[VOICEVOX公式GitHub](https://github.com/VOICEVOX)

[VOICEVOX COREインストール](https://ponkichi.blog/raspberry-voicevox/#st-toc-h-4)

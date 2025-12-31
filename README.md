# ros2 西暦変換
![test](https://github.com/MisonoToma/era_converter/actions/workflows/test.yml/badge.svg)
ロボットシステム学課題2

## 内容

- 片方の端末で西暦（例:2005）を送信し、もう片方の端末で受信し日本の元号（例:昭和・平成・令和）に変換して表示するプログラムです. 

## 実行方法
片方の端末
```
$ ros2 run era_converter era_publisher
```
もう一つの端末
```
$ ros2 run era_converter era_subscriber
```

## 使用環境

- Ubuntu-24.04 LTS

## 必要なソフトウェア

- gcc
- gccのバージョン: 13.3.0

## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
- このパッケージのコードは、[このスライド](https://ryuichiueda.github.io/slides_marp/robosys2025/lesson7.html)のものを、本人の許可を得て自身の著作としたものです.
- © 2025 Toma Misono

## 参考文献

- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson8.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson9.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson10.html

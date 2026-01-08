# ros2 西暦変換
![test](https://github.com/MisonoToma/era_converter/actions/workflows/test.yml/badge.svg)
ロボットシステム学課題2

## 内容

- 片方の端末で西暦の年（例:1926）を送信し、もう片方の端末で受信し日本の元号（例:昭和1年）に変換して表示するプログラムである. 

## ノード
- `era_publisher`というノードは西暦の年を生成して送信する. 
- `era_subscriber`というノードは受信した年を日本の西暦に変換して表示する
- `year`という`std_msgs/msg/Int32`型のトピックは今回使う西暦の年を持っている. 

- `era_publisher`が1926年を初期値とし1 秒ごとに1年ずつ年を`year`に送信する. 

## 実行方法と実行結果
実行方法
```
$ ros2 launch era_converter era.launch.py
```
実行結果(一部分)
```
Publish: 1926
Received: 1926 → 昭和1年
Publish: 1927
Received: 1927 → 昭和2年
```
- 2026年を超えた場合は1926年に戻してループする.

## 使用環境

- Ubuntu-24.04 LTS

## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
- このパッケージのコードは、[このスライド](https://ryuichiueda.github.io/slides_marp/robosys2025/lesson7.html)のものを、本人の許可を得て自身の著作としたものです.
- © 2025 MisonoToma

## 参考文献

- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson8.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson9.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson10.html

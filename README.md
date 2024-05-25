# 小型の模擬人工衛星 CanSat 製作（期間：2022/4 ~ 12）

<ins>機体</ins>
+ パラフォイル (機体制御)
+ スタビライザー (パラフォイル展開補助機構)

<ins>使用モジュール詳細</ins>
+ Raspberry Pi 3 model B
+ GPS (AE-GYSFDMAXB)
+ サーボモータ (MG996R)
+ 3端子レギュレータ (L7806CV)
+ 9軸センサ (BMX055)

<ins>コード詳細</ins> (FunSat2022_code)

使用言語：Python
+ bmx055.py
  + 9軸センサから加速度データを取得するコード
+ Controller.py
  + GPS値からゴールまでの誤差や角度等を算出するコード
    + def set_goal(self, gps_x, gps_y)
      + 機体の座標から、最も近いゴールの座標を返す
      + 座標 = (緯度，経度)
    + def dis_gps(self, old_x, old_y, now_x, now_y, dir_x, dir_y)
      + 機体の進行方向を計算
      + 機体がゴールと左右どちらにずれているかの値を返す
+ GPS.py
  + GPS値を取得するコード
+ servo.py
  + サーボモータを制御するコード
  + 引数 pin に GPIO ピン番号を入力
    + def write(self, angle)
      + 引数 angle にサーボモータを回す角度 (0° ~ 180°) を指定
+ main.py
  + メインコード

## 株式会社 植松電機 様 主催「スペースプローブコンテスト」に参加 (2022/9/17)

+ チーム名「FUNSat」(8名で参加)
+ 方式：フライバック
  + 上空約 100m からドローンで機体を投下

コンテスト結果 https://spc.uematsudenki.com/wp/2022result/

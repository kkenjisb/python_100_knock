# 問題 83 csv のリスト型読み込み
#
# 標準ライブラリの csv モジュールをインポートしてください。
# カレントディレクトリの csv 形式のテキストファイル "test.csv" を読み込み、
# カンマ部分で分割したリストを 1 行ずつ出力してください。
#
# 学習用サンプルは questions/data/q083_test.csv に置いてあります。

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import csv

def main() -> None:
    with open("questions/data/q083_test.csv", "r", newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    main()

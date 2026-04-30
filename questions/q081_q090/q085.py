# 問題 85 csv の辞書型読み込み
#
# 標準ライブラリの csv モジュールをインポートしてください。
# カレントディレクトリの csv 形式のテキストファイル "test.csv" を読み込み、
# ヘッダ行をキーとする辞書を 1 行ずつ出力してください。
#
# 学習用サンプルは questions/data/q085_test.csv に置いてあります。

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import csv
def main() -> None:
    with open("questions/data/q085_test.csv", "r") as file:
        csv_dict_reader = csv.DictReader(file)
        for row in csv_dict_reader:
            print(row)

if __name__ == "__main__":
    main()

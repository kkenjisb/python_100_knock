# 問題 97 辞書を使った文字列のカウント
#
# テキストファイルを読み込み、その中に現れる各文字の出現回数を全て表示してください。
# - main() はカレントディレクトリの input.txt を読み込んでください。

# - 文字の初出順に、print(char, count) で 1 行ずつ出力してください。

# - 学習用サンプルは questions/data/q097_input.txt に置いてあります。

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

def main() -> None:
    with open("questions/data/q097_input.txt", "r") as file:
        text = file.read()
    count_dct = {}
    for val in text:
        if val in count_dct:
            count_dct[val] += 1
        else:
            count_dct[val] = 1
            
    for char, count in count_dct.items():
        print(char, count)


if __name__ == "__main__":
    main()

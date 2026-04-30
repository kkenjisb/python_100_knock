# 問題 82 csv のリスト型書き込み
#
# 標準ライブラリの csv モジュールをインポートしてください。
# 次の変数 lst の情報をカレントディレクトリのテキストファイル "test.csv" に
# カンマで区切られた csv 形式で書き込んでください。
#
# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

import csv

def main() -> None:
    lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    # newline='' を指定しないと空行が挿入される（\r\n の二重変換防止）
    with open("test.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lst)
    pass

if __name__ == "__main__":
    main()

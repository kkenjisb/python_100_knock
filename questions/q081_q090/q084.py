# 問題 84 csv の辞書型書き込み
#
# 標準ライブラリの csv モジュールをインポートしてください。
# 次の変数 lst の情報をカレントディレクトリのテキストファイル "test.csv" に
# ヘッダ行を持つ csv 形式で書き込んでください。
#
# lst = [
#     {'id': '0001', 'name': 'admin'},
#     {'id': '0002', 'name': 'guest'},
#     {'id': '0003', 'name': 'test'},
# ]

import csv
def main() -> None:
    lst = [
        {'id': '0001', 'name': 'admin'},
        {'id': '0002', 'name': 'guest'},
        {'id': '0003', 'name': 'test'},
    ]
    # newline='' を指定しないと空行が挿入される（\r\n の二重変換防止）
    with open("test.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, ["id", "name"])
        writer.writeheader()
        writer.writerows(lst)

if __name__ == "__main__":
    main()

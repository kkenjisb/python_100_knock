# 問題 88 pprint
#
# 標準ライブラリの pprint モジュールから pprint 関数をインポートしてください。
# 次の変数 lst を print 関数と pprint 関数でそれぞれ表示してください。
#
# lst = [
#     {'id': '0001', 'name': 'admin'},
#     {'id': '0002', 'name': 'guest'},
#     {'id': '0003', 'name': 'test'},
# ]

from pprint import pprint
def main() -> None:
    lst = [
        {'id': '0001', 'name': 'admin'},
        {'id': '0002', 'name': 'guest'},
        {'id': '0003', 'name': 'test'},
    ]
    print(lst)
    pprint(lst)

if __name__ == "__main__":
    main()

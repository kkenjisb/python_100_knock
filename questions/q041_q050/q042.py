# 問題 42 辞書のキーと値
#
# 変数 dct に辞書 {'id': '0001', 'name': 'guest'} を代入してください。
# 変数 dct に含まれるキーと値の組を取得し、for 文を用いて順番に全て print 関数で(key, value)を出力してください。


def main() -> None:
    dct = {'id': '0001', 'name': 'guest'}
    for key, value in dct.items():
        print(key, value)

if __name__ == "__main__":
    main()

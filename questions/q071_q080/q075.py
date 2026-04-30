# 問題 75 from と import
#
# from キーワードを使って datetime モジュールから date クラスをインポートしてください。
# date クラスの today メソッドで現在日付のオブジェクトを取得し、
# print 関数で出力してください。
# - 取得した date オブジェクトをそのまま 1 回 print してください。

from datetime import date
def main() -> None:
    print(date.today())

if __name__ == "__main__":
    main()

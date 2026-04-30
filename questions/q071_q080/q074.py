# 問題 74 標準ライブラリの使用
#
# import キーワードを使って標準ライブラリの datetime モジュールをインポートしてください。
# datetime モジュールの datetime クラスのクラスメソッド now を実行し、
# 取得した現在時刻のオブジェクトを print 関数で出力してください。
# - 取得した datetime オブジェクトをそのまま 1 回 print してください。

import datetime
def main() -> None:
    print(datetime.datetime.now())

if __name__ == "__main__":
    main()

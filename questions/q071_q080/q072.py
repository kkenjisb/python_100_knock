# 問題 72 実行中モジュールのパッケージ
#
# マジック変数 __package__ を使用して、
# 実行している Python ファイルが属しているパッケージ名を表示してください。
# - 単体スクリプト相当を想定し、main() では None を print してください。


def main() -> None:
    print(__package__)

if __name__ == "__main__":
    main()

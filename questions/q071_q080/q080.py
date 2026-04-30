# 問題 80 ファイルの読み取り
#
# カレントディレクトリにあるファイル "test.txt" の内容を読み取り、print 関数で出力してください。
# ただし、ファイルが存在しない場合は "ファイルが存在しません" と出力してください。


def main() -> None:
    try:
        with open('test.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("ファイルが存在しません")

if __name__ == "__main__":
    main()

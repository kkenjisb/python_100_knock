# 問題 78 ファイルへの書き込み
#
# 文字列 "Hello, World!" を Python でカレントディレクトリのファイル "test.txt" に書き込んでください。
# ただし、同名のファイルが存在する場合、既存のテキストデータを無視して書き込んだ値で上書きしてください。

def main() -> None:
    with open('test.txt', 'w') as file:
        file.write('Hello, World!')

if __name__ == "__main__":
    main()

# 問題 79 ファイルへの追記
#
# 文字列 "Hello, World!" を Python でカレントディレクトリのファイル "test.txt" に書き込んでください。
# ただし、同名のファイルが存在する場合は既存のテキストデータを保持し、
# 末尾に追記する形で書き込んでください。


def main() -> None:
    with open('test.txt', 'a') as file:
        file.write('Hello, World!')

if __name__ == "__main__":
    main()

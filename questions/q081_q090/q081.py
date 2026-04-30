# 問題 81 ファイルの削除
#
# カレントディレクトリにあるファイル "test.txt" を削除してください。
# ただし、ファイルが存在しない場合は "ファイルが存在しません" と表示してください。

from pathlib import Path
def main() -> None:
    file_path = Path("test.txt")
    if file_path.exists():
        file_path.unlink()
    else:
        print("ファイルが存在しません")

if __name__ == "__main__":
    main()

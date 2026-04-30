# 問題 77 ファイルの存在確認
#
# 標準ライブラリ pathlib モジュールから Path クラスをインポートしてください。
# カレントディレクトリに "test.txt" というファイルが存在するかどうかを判定し、
# 結果を True または False で出力してください。

from pathlib import Path
def main() -> None:
    filepath = Path('test.txt')
    print(filepath.exists())

if __name__ == "__main__":
    main()

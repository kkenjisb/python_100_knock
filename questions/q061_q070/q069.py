# 問題 69 自作モジュールの使用
#
# 次のような関数 sample が定義されたモジュール import_test を作成してください。
# そのモジュールを別のモジュールからインポートし、sample 関数を呼び出してください。
#
# def sample():
#     print('Hello World')
# - import_test.py は q069.py と同じディレクトリに作成してください。
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import questions.q061_q070.import_test as import_test

def main() -> None:
    import_test.sample()

if __name__ == "__main__":
    main()

# 問題 70 自作ライブラリの使用
#
# 前問で作成したモジュール import_test を含むライブラリ library_test を作成してください。
# そのライブラリのモジュール import_test を別のモジュールからインポートし、sample 関数を呼び出してください。
# - library_test/__init__.py と library_test/import_test.py を作成してください。

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from questions.q061_q070.library_test import import_test

def main() -> None:
    import_test.sample()

if __name__ == "__main__":
    main()

# python_100_knock

Qiita の Python 入門100本ノック をローカルの Python と pytest で進めるための学習用リポジトリです。

対象記事:
https://qiita.com/SollaUmiyama/items/e57c2cc044b266ee2b8d

## 前提

- VS Code からこのフォルダを開いていること
- Python が使えること

## 使い方

pytest のインストール:

```bash
python -m pip install -r requirements-dev.txt
```

テストの実行:

```bash
python -m pytest tests --color=yes
```

VS Code の Test Explorer:

- このワークスペースは VS Code の pytest 設定済みなので、xscodeのテストエクスプローラーからそのままテスト実行できます
- 左の Testing ビューを開くと、tests 配下のテストが一覧表示されます
- 問題単位でテストを実行したい場合は、各 `test_q001` のような項目から個別実行できます
- まとめて確認したい場合は、ファイル単位または全体実行もできます
- CLI で `python -m pytest ...` を打たなくても、VS Code 上で学習を進められます

たとえば問題 1 を試すなら、次を実行します。

```bash
python questions/q001_q010/q001.py
```

## ディレクトリ構成

- questions 配下に 10 問ずつ問題ファイルを配置しています
- tests 配下に pytest を配置しています
- questions/data 配下に一部問題で使うサンプルデータを配置しています

## 補足

- 問題ファイルは main() を定義し、`if __name__ == "__main__":` から実行できる形にしています
- 問題 89 の tkinter メッセージボックスは GUI が必要です
- それ以外の標準入出力ベースの問題は、ローカル実行と pytest で進められます
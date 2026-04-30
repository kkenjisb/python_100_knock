# 問題 15 部分文字列
#
# 文字列 "Python" を変数に格納し、最初の 2 文字を抽出して print 関数で出力してください。


def main() -> None:
    text = "Python"
    print(text[:2])

if __name__ == "__main__":
    main()

"""
$ python questions/q011_q020/q015.py
Py
"""
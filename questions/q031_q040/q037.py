# 問題 37 タプルの結合と長さ
#
# 2 つのタプル (1, 2) と (3, 4) を結合してできるタプル (1, 2, 3, 4) を
# 変数 tpl に代入してください。
# 変数 tpl とその長さを print 関数で出力してください。


def main() -> None:
    tpl1 = 1, 2
    tpl2 = 3, 4
    tpl = tpl1 + tpl2
    print(tpl)
    print(len(tpl))

if __name__ == "__main__":
    main()

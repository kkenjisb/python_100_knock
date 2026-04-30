# 問題 20 リストの追加
#
# 変数 lst にリスト [1, 2, 3] を代入してください。
# 変数 lst の末尾に数値 4 を追加してできるリスト [1, 2, 3, 4] を print 関数で出力してください。


def main() -> None:
    lst = [1, 2, 3]
    lst.append(4)
    print(lst)

if __name__ == "__main__":
    main()

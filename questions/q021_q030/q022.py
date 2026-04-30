# 問題 22 リストの削除
#
# 変数 lst にリスト [1, 2, 3] を代入してください。
# 変数 lst から数値 2 を削除してできるリスト [1, 3] を print 関数で出力してください。


def main() -> None:
    lst = [1, 2, 3]
    lst.pop(1)
    print(lst)

if __name__ == "__main__":
    main()

# 問題 23 リストの結合
#
# 2 つのリスト [1, 2] と [3, 4] を結合してできるリスト [1, 2, 3, 4] を print 関数で出力してください。


def main() -> None:
    lst1 = [1, 2]
    lst2 = [3, 4]
    lst = lst1 + lst2
    print(lst)

if __name__ == "__main__":
    main()

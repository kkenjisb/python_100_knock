# 問題 43 リスト内包表記
#
# リスト内包表記を使って、1 以上 10 未満の偶数リストを作成し、そのリストを print で表示してください。


def main() -> None:
    lst = [x for x in range(1, 10) if x % 2 == 0]
    print(lst)

if __name__ == "__main__":
    main()

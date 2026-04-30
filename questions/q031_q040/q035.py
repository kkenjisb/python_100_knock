# 問題 35 while ループ
#
# while ループを使って、10 から 1 まで 1 ずつカウントダウンして出力してください。


def main() -> None:
    x = 10
    while x > 0:
        print(x)
        x = x - 1

if __name__ == "__main__":
    main()

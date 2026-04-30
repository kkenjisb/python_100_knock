# 問題 34 continue の使用
#
# 変数 x に数値 5 を代入してください。
# 0 から 9 までの数を順番に出力する for ループ内で continue を使用し、
# 出力する値が x になった場合の処理をスキップしてください。


def main() -> None:
    x = 5
    for i in range(10):
        if i == x: 
            continue
        print(i)

if __name__ == "__main__":
    main()

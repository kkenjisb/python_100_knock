# 問題 53 ループの終了条件
#
# 正の整数の内、いずれかの桁が 3 である数を小さいほうから 100 個表示してください。


def main() -> None:
    num = 1
    count = 0
    while count < 100:
        if "3" in str(num):
            print(num)
            count += 1
        num += 1

if __name__ == "__main__":
    main()

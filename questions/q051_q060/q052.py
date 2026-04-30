# 問題 52 ループと条件分岐と文字列操作
#
# 100 未満の正の整数の内、いずれかの桁が 3 である数を全て表示してください。


def main() -> None:
    for i in range(1, 100):
        if "3" in str(i):
            print(i)

if __name__ == "__main__":
    main()

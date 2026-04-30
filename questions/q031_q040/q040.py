# 問題 40 集合の要素
#
# 変数 st に集合 {1, 2, 3} を代入してください。
# for 文を用いて変数 st の要素を 1 つずつ出力してください。
# - sorted(st) を for 文で順に出力してください。


def main() -> None:
    st = {1, 2, 3}
    for item in sorted(st):
        print(item)
        
if __name__ == "__main__":
    main()

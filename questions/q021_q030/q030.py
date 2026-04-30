# 問題 30 論理否定
#
# 変数に None を代入してください。
# is 演算子を使って、変数が None であるか判定し、
# None ではない場合に "x は None ではない" を出力してください。


def main() -> None:
    val = None
    if not (val is None):
        print("xはNoneではない")
        

if __name__ == "__main__":
    main()

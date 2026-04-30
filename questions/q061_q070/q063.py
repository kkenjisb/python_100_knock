# 問題 63 関数の戻り値
#
# 引数 a と b を受け取り、それらの和を返す関数 add を定義してください。
# さらに、引数に 1 と 2 を渡して実行し、結果を出力してください。

def add(a:int, b:int) -> int:
    """足し算関数
    値a,bを足して返す。
    Args:
        a (int): 値a
        b (int): 値b

    Returns:
        int: aとbの和
    """
    return a + b

def main() -> None:
    print(add(1, 2))

if __name__ == "__main__":
    main()

# 問題 92 ループと条件分岐の関数
#
# 引数で指定された範囲の正の整数の内、いずれかの桁が 3 である整数の集合を返す関数 find_numbers を作成してください。
# ただし、関数 find_numbers は 2 つの引数 start と end を持ち、
# start 以上 end 未満の正の整数を対象範囲として扱ってください。

def find_numbers(start:int, end:int) -> set:
    st:set = {i for i in range(start, end) if "3" in str(i)}
    return st

def main() -> None:
    print(sorted(find_numbers(10,50)))

if __name__ == "__main__":
    main()

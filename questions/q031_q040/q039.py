# 問題 39 集合の和集合と共通部分
#
# 変数 x に {1, 2, 3} を代入し、変数 y に {3, 4, 5} を代入してください。
# 変数 x と変数 y の和集合 {1, 2, 3, 4, 5} を計算し、print 関数で出力してください。
# また、変数 x と変数 y の共通部分 {3} を計算し、print 関数で出力してください。
# - 和集合と共通部分は、それぞれ sorted(...) の結果を print してください。


def main() -> None:
    x = {1, 2, 3}
    y = {3, 4, 5}
    
    print(sorted(x.union(y)))
    print(sorted(x.intersection(y)))

if __name__ == "__main__":
    main()


"""
$ python questions/q031_q040/q039.py
[1, 2, 3, 4, 5]
[3]
"""
# 問題 10 エスケープシーケンス
#
# 改行を意味する特殊な文字列 \n を含む文字列 "1\n2\n3" を print 関数で出力し、
# 改行されて表示されることを確認してください。


def main() -> None:
    print("1\n2\n3")

if __name__ == "__main__":
    main()

"""
以下で確認
$ python questions/q001_q010/q010.py
1
2
3
"""
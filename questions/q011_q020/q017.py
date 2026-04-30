# 問題 17 変数のデータ型
#
# type 関数を使って、次の各変数のデータ型を確認してください。
#
# a = 10
# b = 3.14
# c = "Hello, Python!"
# d = True


def main() -> None:
    a = 10
    b = 3.14
    c = "Hello, Python!"
    d = True
    
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

if __name__ == "__main__":
    main()

"""
$ python questions/q011_q020/q017.py
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
"""

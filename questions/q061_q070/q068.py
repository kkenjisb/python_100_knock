# 問題 68 クラスメソッドの作成
#
# 前の問題で作成したクラス SimpleClass に次の 2 つの機能を追加してください。
#
# (1) クラス SimpleClass のインスタンスが作成された回数をクラス変数 count で保持する。
# (2) クラスメソッド print_count が実行されると、クラス変数 count の値を print 関数で表示する。

class SimpleClass():
    count:int = 0
    name:str
    
    def __init__(self, name):
        SimpleClass.count += 1
        self.name = name
        print(f"名前が {name} のオブジェクトを作成しました")

    def print_name(self):
        print(self.name)
    
    @classmethod
    def print_count(cls):
        print(cls.count)

def main() -> None:
    SimpleClass("A")
    simple_class = SimpleClass("B")
    simple_class.print_count()

if __name__ == "__main__":
    main()

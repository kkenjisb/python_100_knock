# 問題 67 メソッドの作成
#
# 前の問題で作成したクラス SimpleClass に次の 2 つの機能を追加してください。
#
# (1) クラス SimpleClass のオブジェクト初期化処理において、
#     引数 name で指定された値をインスタンス変数 name で保持する。
# (2) メソッド print_name が実行されると、
#     インスタンス変数 name の値を print 関数で出力する。

class SimpleClass():
    name:str
    
    def __init__(self, name):
        self.name = name
        print(f"名前が {name} のオブジェクトを作成しました")

    def print_name(self):
        print(self.name)

def main() -> None:
    simple_class = SimpleClass("サンプル")
    simple_class.print_name()

if __name__ == "__main__":
    main()

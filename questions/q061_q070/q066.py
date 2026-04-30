# 問題 66 クラスの作成
#
# 次の条件を満たすクラス SimpleClass を定義し、引数に "サンプル" を指定してオブジェクトを初期化してください。
#
# (1) 初期化を行う際に 1 つの引数 name を受け取る
# (2) 初期化処理で "名前が {name} のオブジェクトを作成しました" と出力する

class SimpleClass():
    def __init__(self, name):
        print(f"名前が {name} のオブジェクトを作成しました")

def main() -> None:
    SimpleClass("サンプル")

if __name__ == "__main__":
    main()

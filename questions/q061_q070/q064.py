# 問題 64 デフォルト引数
#
# デフォルト値 "ゲスト" を設定した引数 name を持ち、
# "ようこそ、{name} さん" と出力する関数 welcome_message を定義してください。
# 定義した関数 welcome_message を次の 2 通りで実行してください。
#
# (1) 引数を指定せずに呼び出す
# (2) 引数に "管理者" を指定して呼び出す

def welcome_message(name:str = "ゲスト") -> None:
    print(f"ようこそ、{name} さん")

def main() -> None:
    welcome_message()
    welcome_message("管理者")

if __name__ == "__main__":
    main()

# 問題 98 特定条件の文字列結合クラス
#
# 変数 target_list にリスト [1, 2, 3, None, 5, None, 7] を代入してください。
# 次の条件を満たすクラスを作成し、変数 target_list の None でない要素を
# 文字列 "&" で結合した文字列 "1&2&3&5&7" を出力してください。
#
# クラス名: StringJoiner
#
# 概要:
# 追加されたデータを文字列として保持し、指定された区切り文字でそれらを結合する機能を提供します。
#
# インスタンス変数:
# 1. items: 追加されたデータを文字列として保持するためのリストデータです。
#
# メソッド:
# 1. __init__(self): インスタンス変数 items を空のリストに初期化します。
# 2. append(self, item): 引数 item が None でない場合、文字列に変換してインスタンス変数 items に追加します。
# 3. join(self, delimiter): 引数で指定された文字列 delimiter でインスタンス変数 items を結合した文字列を返します。
#    引数 delimiter は省略可能で、デフォルト値は空文字列です。

class StringJoiner:
    items: list
    
    def __init__(self):
        self.items = []
        
    def append(self, item):
        if item is not None:
            self.items.append(str(item))

    def join(self, delimiter:str = ''):
        return delimiter.join(self.items)
    

def main() -> None:
    target_list = [1, 2, 3, None, 5, None, 7]
    string_joinner = StringJoiner()
    for target in target_list:
        string_joinner.append(target)
    
    print(string_joinner.join("&"))

if __name__ == "__main__":
    main()

# 問題 96 辞書の操作関数
#
# 引数で与えられた辞書のキーと値を逆にした辞書を返す関数 reverse_dict を作成してください。
# ただし、処理に失敗した場合は None を返してください。
# - 値が重複する場合や、値をキーにできない場合は None を返してください。

def reverse_dict(dct:dict) -> dict | None:
    try:
        reversed = {value: key for key, value in dct.items()}
    except:
        return None
    
    # valueが重複した場合は上書きしてしまい総数が合わないときは、Noneを返す。
    if len(reversed) != len(dct):
        return None
    
    return reversed

def main() -> None:
    # 正常時チェック
    print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))
    
    # 異常値チェック
    # valueがオブジェクト系
    print(reverse_dict({'a': 1, 'b': 2, 'c': {3}}))
    # value重複
    print(reverse_dict({'a': 1, 'b': 2, 'c': 1}))
    # 辞書型でない
    print(reverse_dict('not a dict'))

if __name__ == "__main__":
    main()

# 問題 99 リストの補正と補正情報
#
# 変数 lst にリスト [1, 2, 3, None, 5, None, 7] を代入してください。
# 変数 lst の要素の値が偶数でない場合は 2 倍したリスト converted_list を作成してください。
# ただし、偶数であるかどうかは 2 で割った余りが 0 かどうかで判定し、
# 判定に失敗した要素は 0 に変換してください。
# このとき、変換を行った情報を次のようなリストで保持し、pprint 関数で出力してください。
#
# [
#     {'index': 0, 'from': 1, 'to': 2},
#     {'index': 2, 'from': 3, 'to': 6},
#     {'index': 3, 'from': None, 'to': 0},
#     {'index': 4, 'from': 5, 'to': 10},
#     {'index': 5, 'from': None, 'to': 0},
#     {'index': 6, 'from': 7, 'to': 14},
# ]
# - main() は converted_list を return し、補正情報の一覧は pprint してください。


def main() -> None:
    pass

if __name__ == "__main__":
    main()

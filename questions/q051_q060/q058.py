# 問題 58 リストと文字列
#
# 変数 target_list にリスト [1, 2, 3, None, 5, None, 7] を代入してください。
# 変数 target_list の None でない要素を抽出し、
# 文字列 "&" で結合した文字列 "1&2&3&5&7" を出力してください。


def main() -> None:
    target_list = [1, 2, 3, None, 5, None, 7]
    int_str_list = [str(x) for x in target_list if x is not None]
    
    print("&".join(int_str_list))

if __name__ == "__main__":
    main()

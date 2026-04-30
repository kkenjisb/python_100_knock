# 問題 57 文字列のカウント
#
# 変数 target_text に文字列 "hello" を代入してください。
# 変数 target_text に含まれる各文字の出現回数をカウントし、
# 文字と出現回数の組を全て表示してください。
# - 文字の初出順に、print(char, count) で 1 行ずつ出力してください。


def main() -> None:
    target_text = "hello"
    str_counter = {}
    for str in target_text:
        str_counter[str] = str_counter[str] + 1 if str in str_counter else 1
    
    for str, counter in str_counter.items():
        print(str, counter)
        

if __name__ == "__main__":
    main()

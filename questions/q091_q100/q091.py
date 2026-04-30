# 問題 91 九九の計算とファイル操作
#
# 計算結果のいずれかの桁が 3 である九九の計算式を
# カレントディレクトリのテキストファイル "output.txt" に書き出してください。
# 作成する計算式は次のような書式とします。
#
# 1 × 3 = 3
# 3 × 1 = 3
# 4 × 8 = 32
# 4 × 9 = 36
# ...
# 9 × 7 = 63
# - 3 を含むかどうかは、式の結果 c のみを判定対象にしてください。


def main() -> None:
    
    texts = [
        f"{x} × {y} = {x * y}"
        for x in range(1, 10)
        for y in range(1, 10)
        if "3" in str(x * y)
    ]
    write_text = "\n".join(texts)            
    with open("output.txt", "w") as file:
        file.write(write_text)
        
if __name__ == "__main__":
    main()

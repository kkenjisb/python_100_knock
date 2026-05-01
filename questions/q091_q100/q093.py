# 問題 93 ループの終了条件
#
# コマンドラインに "1桁の整数を入力してください" と表示し、ユーザの入力を取得してください。
# ユーザが入力した値を x として、いずれかの桁が x に一致する正の整数を小さいほうから 10 個表示してください。
# ただし、入力された値が 1 桁の整数でない場合は、
# ユーザに入力を求める処理に戻って処理を継続してください。
# - 有効入力は 0 から 9 の 1 文字数字だけとします。

def checkOneDigitStr(x:str | None)-> bool:
    return isinstance(x, str) and len(x) == 1 and x.isdigit()

def main() -> None:
    input_str = None
    while not(checkOneDigitStr(input_str)):
        input_str = input("1桁の整数を入力してください")

    num = 1
    count = 0
    while count < 10:
        if input_str in str(num):
            print(num)
            count += 1
        num += 1

if __name__ == "__main__":
    main()

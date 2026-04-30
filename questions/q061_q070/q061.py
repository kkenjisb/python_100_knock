# 問題 61 関数の定義
#
# 呼び出されると "Hello World" と出力する関数 sample を定義し、
# その関数を 3 回呼び出してください。

def sample() -> None:
    print("Hello World")

def main() -> None:
    for _ in range(3):
        sample()

if __name__ == "__main__":
    main()

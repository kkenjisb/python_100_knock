# 問題 51 九九の計算表示
#
# 2 重の for 文を使って、次のような九九の計算を print 関数で出力してください。
#
# 1 × 1 = 1
# 1 × 2 = 2
# ...
# 9 × 9 = 81
# - 各行の書式は "a × b = c" に統一してください。


def main() -> None:
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} × {j} = {i * j}")

if __name__ == "__main__":
    main()

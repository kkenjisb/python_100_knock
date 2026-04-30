# 問題 56 辞書の操作
#
# 変数 ascii_dict に辞書 {'0x30': '0', '0x40': '@', '0x50': 'P'} を代入してください。
# 変数 ascii_dict のキーと値を逆にした辞書 {'0': '0x30', '@': '0x40', 'P': '0x50'} を作成し、
# print 関数で出力してください。


def main() -> None:
    ascii_dict = {'0x30': '0', '0x40': '@', '0x50': 'P'}
    reverted_dict = {value: key for key, value in ascii_dict.items()}
    print(reverted_dict)
    
    
if __name__ == "__main__":
    main()

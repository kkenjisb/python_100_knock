# 問題 89 メッセージボックス
#
# 標準ライブラリの tkinter モジュールのサブモジュール messagebox から
# showinfo 関数と askyesno 関数をインポートしてください。
# それぞれの関数を使用して、"タイトル" と "メッセージ" を設定したメッセージウィンドウを表示してください。

from tkinter.messagebox import showinfo, askyesno
def main() -> None:
    showinfo("タイトル", "メッセージ")
    askyesno("タイトル", "メッセージ")

if __name__ == "__main__":
    main()

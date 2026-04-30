# 問題 90 ログ出力
#
# 標準ライブラリの logging モジュールをインポートし、下記の basicConfig を実行してください。
# ロガーオブジェクトを使用して、情報ログ「正常終了しました」と
# 異常ログ「予期せぬエラーが発生しました」をログ出力してください。
#
# logging.basicConfig(
#     level=logging.INFO,
#     format='[%(asctime)s][%(levelname)-5s] %(message)s',
# )

import logging

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)-5s] %(message)s',
    )
    
    logger = logging.getLogger(__name__)
    logger.info("正常終了しました")
    logger.error("予期せぬエラーが発生しました")

if __name__ == "__main__":
    main()

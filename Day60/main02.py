import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding="utf-8"
)


logging.info("程式啟動")
logging.warning("記憶體不足")
logging.error("資料讀取失敗")
try:
    number = 10 / 0
except ZeroDivisionError as error:
    logging.error(f"計算失敗：{error}")
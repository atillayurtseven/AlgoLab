from algolab import AlgoLab
import pandas as pd
import numpy as np
import datetime
import os
from dotenv import load_dotenv
import time

# USER INFO
load_dotenv()
API_KEY = os.getenv('API_KEY_A')
USERNAME = os.getenv('TC_PASS')
PASSWORD = os.getenv('DB_PASS')
if __name__ == "__main__":
    symbol = "GARAN"
    period = "10080" # 1 hafta
    algo_class = AlgoLab(api_key=API_KEY, username=USERNAME, password=PASSWORD)
    candle = algo_class.GetCandleData(symbol, period)
    if candle:
        succ = candle["success"]
        if succ:
            ohlc = []
            content = candle["content"]
            for i in range(len(content)):
                d = content[i]["date"]
                try:
                    dt = datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                except:
                    dt = datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%d %H:%M:%S")
                o = content[i]["open"]
                h = content[i]["high"]
                l = content[i]["low"]
                c = content[i]["close"]
                ohlc.append([dt, o, h, l, c])
            # oluşturduğumuz listi pandas dataframe'e aktarıyoruz
            df = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close"], data=np.array(ohlc))
            print(df.tail())

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        algo_class.kill_self()

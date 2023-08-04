from algolab import AlgoLab
import pandas as pd
import numpy as np
import datetime

# USER INFO
API_KEY = "API_KEY"
USERNAME = "TC_KİMLİK_NO"
PASSWORD = "DENİZBANK_ŞİFRENİZ"

if __name__ == "__main__":
    symbol = "GARAN"
    period = "60" # 60 dk
    d = AlgoLab(api_key=API_KEY, username=USERNAME, password=PASSWORD)
    # Login olarak, token alıyoruz
    if d.LoginUser():
        # token ile hash algoritmasını alıyoruz
        if d.LoginUserControl():
            # GARAN hissesinin 60 dk'lık geçmişini alıyoruz. DİKKAT: Seans içindeyseniz son bar henüz kapanmamıştır.
            candle = d.GetCandleData(symbol, period)
            if candle:
                print(candle)
                try:
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
                        df = pd.DataFrame(columns=["date", "open", "high", "low", "close"], data=np.array(ohlc))
                        print(df.tail())
                except Exception as e:
                    print(f"Hata oluştu: {e}")
        else:
            print("Login kontrolü başarısız oldu")
    else:
        print("Login başarısız oldu")

    print("Sonlandırıldı")

from algolab import AlgoLab
from algolab_socket import AlgoLabSocket
import json
import time

# USER INFO
API_KEY = "API_KEY"
USERNAME = "TC_KİMLİK_NO"
PASSWORD = "DENİZBANK_ŞİFRENİZ"

if __name__ == "__main__":
    symbol = "GARAN"
    period = "60" # 60 dk
    algo = AlgoLab(api_key=API_KEY, username=USERNAME, password=PASSWORD, auto_login=True)
    soket = AlgoLabSocket(algo.api_key, algo.hash, "T")
    soket.connect()
    while not soket.connected:
        time.sleep(0.05)

    data = {"Type": "T", "Symbols": ["GARAN", "TSKB"]}
    soket.send(data)

    i = 0
    while soket.connected:
        data = soket.recv()
        i += 1
        if data:
            try:
                msg = json.loads(data)
                print(msg)
            except:
                print("error 1")
                soket.close()
                break
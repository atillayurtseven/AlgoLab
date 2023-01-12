from deniz_yatirim import AlgoLab
from algolab_socket import AlgoLabSocket

# KULLANICI BİLGİSİ

API_KEY = "API_KEY"
USERNAME = "TC_KİMLİK_NO"
PASSWORD = "DENİZBANK_ŞİFRENİZ"

def process_msg(msg):
    try:
        t = msg["Type"]
        content = msg["Content"]
        print(content)
    except:
        pass

if __name__ == "__main__":
    algo = AlgoLab(api_key=API_KEY, username=USERNAME, password=PASSWORD, auto_login=True)
    soket = AlgoLabSocket(algo.api_key, algo.hash, "T", callback=process_msg)

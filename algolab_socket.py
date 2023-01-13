import hashlib, json, datetime, subprocess, ssl, socket
from threading import Thread
import pandas as pd
from websocket import create_connection
from config import *

class AlgoLabSocket():
    def __init__(self, api_key, hash, type, verbose=True, callback=None):
        """
        :String api_key: API_KEY
        :String hash: LoginUser'dan dönen Hash kodu
        :String type: T: Tick Paketi (Fiyat), D: Depth Paketi (Derinlik), O: Emir Statüsü
        :Obj type: callback: Soketin veriyi göndereceği fonksiyon
        """
        self.verbose = verbose
        self.callback = callback
        self.arbitraj = {}
        self.thread_running = False
        self.kurum = {}
        self.hisse = {}
        self.df = pd.DataFrame(columns=["Date", "Hisse", "Yon", "Fiyat", "Lot", "Deger", "Usd", "Alici", "Satici"])
        self.usdtry = 0.0
        self.ws = None
        self.api_key = api_key
        self.hash = hash
        self.type = type
        self.data = self.api_key + api_hostname + "/ws"
        self.checker = hashlib.sha256(self.data.encode('utf-8')).hexdigest()
        self.request_time = datetime.datetime.now()
        self.headers = {
            "APIKEY": self.api_key,
            "Authorization": self.hash,
            "Checker": self.checker
        }
        self.thread = Thread(target=self.websocket_thread)
        self.thread.start()

    def load_ciphers(self):
        output = subprocess.run(["openssl", "ciphers"], capture_output=True).stdout
        output_str = output.decode("utf-8")
        ciphers = output_str.strip().split("\n")
        return ciphers[0]

    def websocket_thread(self):
        if self.verbose:
            print("Socket bağlantısı kuruluyor...")
        while True:
            data = {
                "Type": self.type,
                "Token": self.hash
            }
            ciphers = self.load_ciphers()
            context = ssl.create_default_context()
            context.minimum_version = ssl.TLSVersion.TLSv1_2
            context.set_ciphers(ciphers)
            sock = socket.create_connection((hostname, 443))
            ssock = context.wrap_socket(sock, server_hostname=hostname)
            self.ws = create_connection(socket_url, socket=ssock, header=self.headers)
            self.ws.send(json.dumps(data))
            self.thread_running = True
            if self.verbose:
                print("Socket bağlantısı başarılı.")
            self.fetch_data()

    def fetch_data(self):
        while self.thread_running:
            try:
                data = self.ws.recv()
                msg = {}
                if data != "":
                    msg = json.loads(data)
            except Exception as e:
                print(f"Socket Hatası: {e}")
                self.thread_running = False
            else:
                if self.callback != None:
                    self.callback(msg)
        try:
            if self.ws:
                self.ws.close()
        except:
            pass

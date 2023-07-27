# -*- coding: utf-8 -*-
import hashlib, json, datetime, subprocess, ssl, socket
import pandas as pd
from websocket import create_connection, WebSocketTimeoutException
from config import *

class AlgoLabSocket():
    def __init__(self, api_key, hash, verbose=True, callback=None):
        """
        :String api_key: API_KEY
        :String hash: LoginUserControl'den dönen Hash kodu
        :Obj callback: Soketin veriyi göndereceği fonksiyon
        """
        self.verbose = verbose
        self.callback = callback
        self._connected = False
        self.thread_running = False
        self.df = pd.DataFrame(columns=["Date", "Hisse", "Yon", "Fiyat", "Lot", "Deger", "Usd", "Alici", "Satici"])
        self.usdtry = 0.0
        self.ws = None
        self.api_key = api_key
        self.hash = hash
        self.data = self.api_key + api_hostname + "/ws"
        self.checker = hashlib.sha256(self.data.encode('utf-8')).hexdigest()
        self.request_time = datetime.datetime.now()
        self.headers = {
            "APIKEY": self.api_key,
            "Authorization": self.hash,
            "Checker": self.checker
        }

    def close(self):
        self._connected = False
        self.ws = None

    def connect(self):
        if self.verbose:
            print("Socket bağlantısı kuruluyor...")
        try:
            ciphers = self.load_ciphers()
        except:
            pass
        context = ssl.create_default_context()
        context.set_ciphers("DEFAULT")
        try:
            sock = socket.create_connection((hostname, 443))
            ssock = context.wrap_socket(sock, server_hostname=hostname)
            self.ws = create_connection(socket_url, socket=ssock, header=self.headers)
            self._connected = True
        except Exception as e:
            self.close()
            print(f"Socket Hatası: {e}")
        if self.verbose:
            print("Socket bağlantısı başarılı.")
            self.verbose = False

    def recv(self):
        try:
            data = self.ws.recv()
        except WebSocketTimeoutException:
            data = ""
        except Exception as e:
            print("Recv Error:", e)
            data = None
            self.close()
        return data

    def send(self, d):
        """
        :param d: Dict
        """
        try:
            data = {"token": self.hash}
            for s in d:
                data[s] = d[s]
            resp = self.ws.send(json.dumps(data))
        except:
            print("Send Error:", e)
            resp = None
            self.close()
        return resp

    def get_connected(self):
        return self._connected

    connected = property(get_connected)
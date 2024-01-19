# -*- coding: utf-8 -*-
import hashlib, json, datetime, ssl, socket
from websocket import create_connection, WebSocketTimeoutException, WebSocketConnectionClosedException
from config import *

class AlgoLabSocket():
    def __init__(self, api_key, hash, verbose=True, callback=None, timeout=0, ping_timer=900):
        """
        :String api_key: API_KEY
        :String hash: LoginUserControl'den dönen Hash kodu
        :Obj callback: Soketin veriyi göndereceği fonksiyon
        """
        self.ping_timer = ping_timer
        self.last_ping = datetime.datetime.now()
        self.timeout = timeout
        self.verbose = verbose
        self.callback = callback
        self._connected = False
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
        context = ssl.create_default_context()
        context.set_ciphers("DEFAULT")
        try:
            if self.timeout > 0:
                sock = socket.create_connection((hostname, 443), timeout=self.timeout)
            else:
                sock = socket.create_connection((hostname, 443))
            ssock = context.wrap_socket(sock, server_hostname=hostname)
            self.ws = create_connection(socket_url, socket=ssock, header=self.headers)
            self._connected = True
            self.last_ping = datetime.datetime.now()
        except Exception as e:
            self.close()
            print(f"Socket Hatası: {e}")
        if self.verbose:
            print("Socket bağlantısı başarılı.")
            #self.verbose = False

    def recv(self):
        try:
            data = self.ws.recv()
        except WebSocketTimeoutException:
            data = ""
        except WebSocketConnectionClosedException:
            print("Connection closed")
            self.close()
            return False
        except Exception as e:
            print("Recv Error:", e)
            self.close()
            return False
        if self.heart_beat:
            r = self.ping()
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
        except Exception as e:
            print("Send Error:", e)
            resp = None
            self.close()
        return resp

    def ping(self):
        data = {"Type": "H"}
        return self.send(data)

    def get_heart_beat(self):
        t = datetime.datetime.now()
        r = (t - self.last_ping).seconds > self.ping_timer
        if r:
            self.last_ping = datetime.datetime.now()
        return r

    def get_connected(self):
        return self._connected

    connected = property(get_connected)
    heart_beat = property(get_heart_beat)

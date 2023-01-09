import hashlib, json, datetime, subprocess, ssl, socket
from threading import Thread
from websocket import create_connection, WebSocketConnectionClosedException
from config import *

class AlgoLabSocket():
    def __init__(self, api_key, hash, type):
        """
        :String api_key: API_KEY
        :String hash: LoginUser'dan dönen Hash kodu
        :String type: T: Tick Paketi (Fiyat), D: Depth Paketi (Derinlik), O: Emir Statüsü
        """
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
        """
        Bilgisayarımızda kayıtlı olan cipherları yüklüyoruz. openssl uygulamasının bilgisayarınızda yüklü olması gerekir
        :return: String
        """
        try:
            output = subprocess.run(["openssl", "ciphers"], capture_output=True).stdout
            output_str = output.decode("utf-8")
            ciphers = output_str.strip().split("\n")
            return ciphers[0]
        except:
            return ""

    def websocket_thread(self):
        """
        Websocket thread program kapanana kadar çalışmaya devam eder. Hatalara ve bağlantı kopmalarını kontrol etmeyi unutmayın.
        """
        try:
            data = {
                "Type": self.type,
                "Token": self.hash
            }

            # SOKET düzeltme bloğu. Şayet çalışmazsa, bu bloğu comment out yapın
            ciphers = self.load_ciphers()
            context = ssl.create_default_context()
            context.minimum_version = ssl.TLSVersion.TLSv1_2
            context.set_ciphers(ciphers)
            sock = socket.create_connection((hostname, 443))
            ssock = context.wrap_socket(sock, server_hostname=hostname)
            self.ws = create_connection(socket_url, socket=ssock, header=self.headers)
            # Blok bitiş

            # yukarıdaki bloğu comment out yaptıysanız, aşağıdaki kodu çalıştırın
            #self.ws = create_connection(socket_url, header=self.headers)

            self.ws.send(json.dumps(data))
            self.thread_running = True

            # okuma döngüsünü çağır
            self.fetch_data()
        except:
            pass

    def fetch_data(self):
        """
        Websocket'ten gelen datayı bu fonksiyonda okuyoruz
        """
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
                self.process_msg(msg)
        try:
            if self.ws:
                self.ws.close()
        except WebSocketConnectionClosedException:
            pass

    def process_msg(self, msg):
        """
        :Dict msg: Socketten dönen mesaj

        Algoritmanızı bu fonksiyon altında geliştirebilirsiniz.
        """
        #print(msg)
        pass
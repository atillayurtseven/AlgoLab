import requests, hashlib, json, base64, inspect
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# USER INFO
API_KEY = "API_KEY"
USERNAME = "TC_KIMLIK_NO"
PASSWORD = "DENIZBANK_HESAP_ŞİFRENİZ"

api_hostname = "https://www.algolab.com.tr"
api_url = api_hostname + "/api"
socket_url = "wss://www.algolab.com.tr/api/ws"

# ENDPOINTS
URL_LOGIN_USER = "/api/LoginUser"
URL_LOGIN_CONTROL = "/api/LoginUserControl"
URL_GETEQUITYINFO = "/api/GetEquityInfo"
URL_GETSUBACCOUNTS = "/api/GetSubAccounts"
URL_INSTANTPOSITION = "/api/InstantPosition"
URL_TODAYTRANSACTION = "/api/TodaysTransaction"
URL_VIOPCUSTOMEROVERALL = "/api/ViopCustomerOverall"
URL_VIOPCUSTOMERTRANSACTIONS = "/api/ViopCustomerTransactions"
URL_SENDORDER = "/api/SendOrder"
URL_MODIFYORDER = "/api/ModifyOrder"
URL_DELETEORDER = "/api/DeleteOrder"
URL_DELETEORDERVIOP = "/api/DeleteOrderViop"
URL_SESSIONREFRESH = "/api/SessionRefresh"
URL_GETCANDLEDATA = "/api/GetCandleData"

class DenizYatirim():
    def __init__(self, verbose=True):
        print("Sistem hazırlanıyor...")
        try:
            self.api_code = API_KEY.split("-")[1]
        except:
            self.api_code = API_KEY
        self.api_key = "API-" + self.api_code
        self.username = USERNAME
        self.password = PASSWORD
        self.api_hostname = api_hostname
        self.api_url = api_url
        self.headers = {"APIKEY": self.api_key}
        self.verbose = verbose
        self.reset()

    def reset(self):
        self.token = ""
        self.new_hour = False
        self.sms_code = ""
        self.hash = ""

    # LOGIN

    def LoginUser(self):
        try:
            if self.verbose:
                print("Login işlemi yapılıyor...")
            f = inspect.stack()[0][3]
            u = self.encrypt(self.username)
            p = self.encrypt(self.password)
            payload = {"Username": u, "Password": p}
            endpoint = URL_LOGIN_USER
            resp = self.post(endpoint=endpoint, payload=payload, login=True)
            login_user = self.error_check(resp, f)
            if not login_user:
                return False
            login_user = resp.json()
            succ = login_user["Success"]
            msg = login_user["Message"]
            content = login_user["Content"]
            if succ:
                self.token = content["token"]
                if self.verbose:
                    print(f"Login başarılı.\nToken: {self.token}")
                    return True
            else:
                if self.verbose:
                    print(f"Login Başarısız. Mesaj: {msg}")
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def LoginUserControl(self):
        try:
            if self.verbose:
                print("Login kontrolü yapılıyor...")
            self.sms_code = input("Cep telefonunuza gelen SMS kodunu girin: ")
            f = inspect.stack()[0][3]
            t = self.encrypt(self.token)
            s = self.encrypt(self.sms_code)
            payload = {'token': t, 'Password': s}
            endpoint = URL_LOGIN_CONTROL
            resp = self.post(endpoint, payload=payload, login=True)
            login_control = self.error_check(resp, f)
            if not login_control:
                return False
            login_control = resp.json()
            succ = login_control["Success"]
            msg = login_control["Message"]
            content = login_control["Content"]
            if succ:
                self.hash = content["Hash"]
                if self.verbose:
                    print(f"Login kontrolü başarılı.\nHash: {self.hash}")
                    return True
            else:
                if self.verbose:
                    print(f"Login kontrolü başarısız.\nMesaj: {msg}")
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def Login(self):
        if self.LoginUser():
            return self.LoginUserControl()

    # REQUESTS

    def SessionRefresh(self):
        try:
            f = inspect.stack()[0][3]
            endpoint = URL_SESSIONREFRESH
            payload = {}
            resp = self.post(endpoint, payload=payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def GetEquityInfo(self, symbol):
        """
        :String symbol: Sembol Kodu Örn: ARCLK
        """
        try:
            f = inspect.stack()[0][3]
            endpoint = URL_GETEQUITYINFO
            payload = {'symbol': symbol}
            resp = self.post(endpoint, payload=payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def GetSubAccounts(self):
        try:
            f = inspect.stack()[0][3]
            end_point = URL_GETSUBACCOUNTS
            resp = self.post(end_point, {})
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def GetInstantPosition(self, sub_account=""):
        try:
            f = inspect.stack()[0][3]
            end_point = URL_INSTANTPOSITION
            payload = {'Subaccount': sub_account}
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def GetTodaysTransaction(self, sub_account=""):
        try:
            f = inspect.stack()[0][3]
            end_point = URL_TODAYTRANSACTION
            payload = {'Subaccount': sub_account}
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def GetViopCustomerOverall(self, sub_account=""):
        try:
            f = inspect.stack()[0][3]
            end_point = URL_VIOPCUSTOMEROVERALL
            payload = {'Subaccount': sub_account}
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def GetViopCustomerTransactions(self, sub_account=""):
        try:
            f = inspect.stack()[0][3]
            end_point = URL_VIOPCUSTOMERTRANSACTIONS
            payload = {'Subaccount': sub_account}
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def GetCandleData(self, symbol, period):
        try:
            f = inspect.stack()[0][3]
            end_point = URL_GETCANDLEDATA
            payload = {
                'symbol': symbol,
                'period': period
            }
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    # ORDERS

    def SendOrder(self, symbol, direction, pricetype, price, lot, sms, email, subAccount):
        """
        :String symbol: Sembol Kodu
        :String direction: İşlem Yönü: BUY / SELL (Alış/Satış)
        :String pricetype: Emir Tipi: piyasa/limit
        :String price: Emir tipi limit ise fiyat girilmelidir. (Örn. 1.98 şeklinde girilmelidir.)
        :String lot: Emir Adeti
        :Bool sms: Sms Gönderim
        :Bool email: Email Gönderim
        :String subAccount: Alt Hesap Numarası “Boş gönderilebilir. Boş gönderilir ise Aktif Hesap Bilgilerini getirir.”

        Örnek Body:
        {
            "symbol": "TSKB",
            "direction": "BUY",
            "pricetype": "limit",
            "price": "2.01",
            "lot": "1",
            "sms": True,
            "email": False,
            "Subaccount": ""
        }
        """
        try:
            f = inspect.stack()[0][3]
            end_point = URL_SENDORDER
            payload = {
                "symbol": symbol,
                "direction": direction,
                "pricetype": pricetype,
                "price": price,
                "lot": lot,
                "sms": sms,
                "email": email,
                "subAccount": subAccount
            }
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def ModifyOrder(self, id, price, lot, viop, subAccount):
        """
        :String id: Emrin ID’ si
        :String price: Düzeltilecek Fiyat
        :String lot: Lot Miktarı (Viop emri ise girilmelidir.)
        :Bool viop: Emrin Viop emri olduğunu belirtir. “Viop emri ise true olmalıdır.”
        :String subAccount: Alt Hesap Numarası “Boş gönderilebilir. Boş gönderilir ise Aktif Hesap Bilgilerini getirir.”

        Örnek Body
        {
            "id":"001VEV",
            "price":"2.04",
            "lot":"0",
            "viop":false,
            "Subaccount":""
        }
        """
        try:
            f = inspect.stack()[0][3]
            end_point = URL_MODIFYORDER
            payload = {
                'id': id,
                'price': price,
                'lot': lot,
                'viop': viop,
                'subAccount': subAccount
            }
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def DeleteOrder(self, id, subAccount):
        """
        :String id: Emrin ID’ si
        :String subAccount: Alt Hesap Numarası “Boş gönderilebilir. Boş gönderilir ise Aktif Hesap Bilgilerini getirir.”

        Örnek Body
        {
            "id":"001VEV",
            "subAccount":""
        }
        """
        try:
            f = inspect.stack()[0][3]
            end_point = URL_DELETEORDER
            payload = {
                'id': id,
                'subAccount': subAccount
            }
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    def DeleteOrderViop(self, id, adet, subAccount):
        """
        :String id: Emrin ID’ si
        :String adet: İptal edilecek adet
        :String subAccount: Alt Hesap Numarası “Boş gönderilebilir. Boş gönderilir ise Aktif Hesap Bilgilerini getirir.”

        Örnek Body
        {
            "id":"001VEV",
            "adet":"1",
            "subAccount":""
        }
        """
        try:
            f = inspect.stack()[0][3]
            end_point = URL_DELETEORDERVIOP
            payload = {
                'id': id,
                'adet': adet,
                'subAccount': subAccount
            }
            resp = self.post(end_point, payload)
            return self.error_check(resp, f)
        except Exception as e:
            print(f"{f}() fonsiyonunda hata oluştu: {e}")

    # TOOLS

    def error_check(self, resp, f):
        try:
            data = resp.json()
            return data
        except:
            print(f"{f}() fonksiyonunda veri tipi hatası. Veri, json formatından farklı geldi:")
            print(resp.text)
            return False

    def encrypt(self, text):
        iv = b'\0' * 16
        key = base64.b64decode(self.api_code.encode('utf-8'))
        cipher = AES.new(key, AES.MODE_CBC, iv)
        bytes = text.encode()
        padded_bytes = pad(bytes, 16)
        r = cipher.encrypt(padded_bytes)
        return base64.b64encode(r).decode("utf-8")

    def make_checker(self, endpoint, payload):
        body = json.dumps(payload)
        """
        if len(payload) > 0:
            body = str(payload)
        else:
            body = ""
        """
        data = self.api_key + self.api_hostname + endpoint + body
        checker = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return checker

    def _request(self, method, url, endpoint, payload, headers):
        response = ""
        if method == "POST":
            response = requests.post(url + endpoint, json=payload, headers=headers)
        return response

    def post(self, endpoint, payload, login=False):
        if not login:
            checker = self.make_checker(endpoint, payload)
            headers = {"APIKEY": self.api_key,
                       "Authorization": self.hash,
                       "Checker": checker}
            url = self.api_url
        else:
            headers = {"APIKEY": self.api_key}
            url = self.api_url
        return self._request("POST", url, endpoint, payload=payload, headers=headers)

if __name__ == "__main__":
    d = DenizYatirim()
    if d.LoginUser():
        if d.LoginUserControl():
            eq = d.GetEquityInfo("ARCLK")
            if eq:
                print(eq)
        else:
            print("Login kontrolü başarısız oldu")
    else:
        print("Login başarısız")
    print("Sonlandırıldı")
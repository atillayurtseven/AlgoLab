hostname = "www.algolab.com.tr"
api_hostname = f"https://{hostname}"
api_url = api_hostname + "/api"
socket_url = f"wss://{hostname}/api/ws"

# MARKETS
MARKETS = {
    "VIP": "BIST30 VIOP",
    "KIYM": "KIYMETLİ MADENLER",
    "FX": "FOREX",
    "IMKBH": "BIST SPOT",
    "IMKBX": "ENDEKS",
    "INTUSD": "",
    "INTEUR": "",
}

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

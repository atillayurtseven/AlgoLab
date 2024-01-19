# ALGOLAB API Documentation

ALGOLAB API 

Versiyon: 1.0.5 

1. ERİŞİM HAZIRLIĞI 

 

API kullanmanız gerekiyorsa, API anahtarını aldıktan sonra bu belgenin ayrıntılarına göre geliştirebilirsiniz. Her 

kullanıcıya 1 adet API Anahtarı oluşturulur. 

İki adet izin mevcuttur. Bu izinler şu şekilde açıklanmaktadır: 

• Canlı Veri Sözleşmesi: Soketten gelen verilerin gecikmeli olmaması için gerekli sözleşmedir. 

• Derinlik Veri Sözleşmesi: Soketten gelen verilere derinlik verilerine erişim sağlayan sözleşmedir. API’ yi 

kullanırken lütfen aşağıdaki bilgileri unutmayın: 

• APIKEY: Rastgele bir algoritma tarafından oluşturulan API işlemlerinin kimliğidir. 

• Internet Bankacılığı Kullanıcı Adı/Müşteri Numarası: Sizin oluşturduğunuz kullanıcı adı veya bankanın size vermiş 

olduğu müşteri numarasıdır. 

• Internet Bankacılığı Şifreniz: Sizin oluşturmuş olduğunuz internet bankacılığı şifresidir. 

• Sms Doğrulama Kodu: Sistemde kayıtlı telefon numaranıza gelen rastgele oluşturulmuş şifredir. 

Erişim Kısıtlaması: 

Bu bölüm temel olarak erişim kısıtlamalarına odaklanmaktadır: 

• Rest API, erişim sıklık sınırını aştığında 429 durumunu döndürür: istek çok sık. 

API Alan Adı: 

İstekler için aşağıdaki url ile erişim sağlanmaktadır. 

• https://www.algolab.com.tr/api 

Soket bağlantısı için aşağıdaki url ile erişim sağlanmaktadır. 

• wss://www.algolab.com.tr/api/ws 

API Doğrulaması: 

Bir istek başlatmak için aşağıdaki bilgiler gerekmektedir; 

APIKEY: API Anahtarıdır. 

Authorization: Kullanıcı girişi yapıldıktan sonraki isteklerde kullanılmaktadır. 

Checker: Her isteğe özel imzadır. Her isteğe göre yeniden oluşturulur. APIKEY + RequestPath + QueryString veya 

Body(GET/POST Methoduna göre değişiklik göstermektedir.) 

• APIKEY: API Anahtarıdır. 

• RequestPath: API yolu. 

• QueryString: İstek URL’ indeki sorgu dizesi (?’den sonraki istek parametresi soru işareti ile birlikte) 

• Body: İstek gövdesine karşılım gelen dize. Body genellikle POST isteğinde olur. 

 

 

Örneğin: 

Portföy bilgisini çekme; 

APIKEY: APIKEY-04YW0b9Cb8S0MrgBw/Y4iPYi2hjIidW7qj4hrhBhwZg= 

Yöntem: POST 

RequestPath: https://www.algolab.com.tr/api/api/Portfolio 

QueryString: Yöntem POST olduğu için Boş 

Body: {"Subaccount":""} 

 

JSON değer olduğu için String’ e dönüştürülerek checker’ ı oluşturacak dizeye eklenir. Checker’ı oluşturacak dize 

aşağıdaki şekildedir. 

APIKEY-

04YW0b9Cb8S0MrgBw/Y4iPYi2hjIidW7qj4hrhBhwZg=https://www.algolab.com.tr/api/api/Portfolio{\"Subaccount\":\"\

"} 

Yukarıdaki string SHA256 hash algoritması ile şifrelenir. Şifrelemede oluşan string değer Checker parametresine yazılır. 

Etkileşim Talebi: 

Tüm istekler Https protokolüne dayalıdır ve istek başlık (Header) bilgilerindeki içerik türü (Content-Type)’nün tamamını 

‘application/json’ olarak ayarlanması gerekmektedir. 

Başarı: 

HTTP durum kodu 200, başarılı bir yanıtı belirtir ve içerik içerebilir. Yanıt içerik içeriyorsa, ilgili dönüş içeriğinde 

görüntülenecektir. 

Başarılı dönen cevaplar aşağıdaki json model’ ine göre döner. 

{ 

"Success":  bool,  //Başarılı  bir  istek  ise  true  cevabı  gelir. 

"Message":  string,  //Eğer  başarısız  bir  istekse  veya  herhangi  bir  hata  olursa  hata  mesajı  döner. "Content":  object  

//Her  fonksiyona  göre  farklı  model  dönmektedir. 

} 

Standart Şartname: 

• Frekans Sınırlama Kuralları 

İstek çok sık olursa, sistem isteği otomatik olarak sınırlandırır ve http başlığında 429 çok fazla istek durum kodunu 

döndürür. Frekans limiti saniyede bir istektir. 

• Talep Formatı 

Şu anda biçimlerde yalnızca iki istek yöntemi vardır: GET ve POST 

a. GET: Parametreler sunucuya queryString yolu ile iletilir. 

b. POST: Parametreler gövde json formatında gönderilerek sunucuya gönderilir. 

 

 

2. RESTAPI 

Kullanıcı Girişi Sms Alma 

 

Internet Bankacılığı bilgileri ile giriş yapmanızı sağlar. İstek sonunda sistemde kayıtlı telefon numaranıza Sms gelir. 

Gelen Sms’ teki kod ile bir sonraki işlem gerçekleştirilecektir. 

Http İsteği  

• 

POST /api/LoginUser 

Http Headers  

 

Content-Type: application/json  

APIKEY: Başvuru Sonucu Alınan APIKEY 

İstek Parametresi 

Aşağıdaki parametreleri AES Algoritmasını kullanarak APIKEY içerisindeki “-” ‘den sonraki string değer ile şifrelemeniz 

gerekmektedir. 

Örneğin: 

APIKEY: APIKEY-04YW0b9Cb8S0MrgBw/Y4iPYi2hjIidW7qj4hrhBhwZg= 

Yukarıdaki APIKEY’ e göre AES Algoritmasında kullanılacak key aşağıdaki şekildedir. 

aes.Key: 04YW0b9Cb8S0MrgBw/Y4iPYi2hjIidW7qj4hrhBhwZg= 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Username 

String 

Kullanıcı Adı/Müşteri Numarası 

Password 

String 

İnternet Bankacılığı Şifresi 

 

Örnek Body: 

{ 

"Username":"YTZ1RF2Q04T/nZThi0JzUA==", 

"Password":"9LHZEiA2AhKsAtM4yOOrEw==" 

} 

Sonuç  

 

Parametre Adı 

Parametre Tipi 

Açıklama 

token 

String 

Sms İçin Gerekli Token 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content":  

{  

"token": "Ys/WhU/D37vO71VIBumDRhZLmkcMlzyb3TKJVWxLlpb/4BByYLNfQ07dEe66P3Ab"  

}  

} 

 

 

Kullanıcı Girişi Oturum Alma 

 

Kullanıcı girişi Sms alma metodunda alınan token ve sistemdeki kayıtlı telefonunuza gelen kod ile hash kodu almanızı 

sağlar. 

Http İsteği  

• 

POST /api/LoginUserControl 

Http Headers  

 

Content-Type: application/json  

APIKEY: Başvuru Sonucu Alınan APIKEY 

İstek Parametresi 

Aşağıdaki parametreleri AES Algoritmasını kullanarak APIKEY içerisindeki “-” ‘den sonraki string değer ile şifrelemeniz 

gerekmektedir. 

Örneğin: 

APIKEY: APIKEY-04YW0b9Cb8S0MrgBw/Y4iPYi2hjIidW7qj4hrhBhwZg= 

Yukarıdaki APIKEY’ e göre AES Algoritmasında kullanılacak key aşağıdaki şekildedir. 

aes.Key: 04YW0b9Cb8S0MrgBw/Y4iPYi2hjIidW7qj4hrhBhwZg= 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

token 

String 

Sms Alma methodundaki token 

Password 

String 

Sms Kodu 

 

Örnek Body: 

{ 

"token":"Ys/WhU/D37vO71VIBumDRhZLmkcMlzyb3TKJVWxLlpb/4BByYLNfQ07dEe66P3Ab", 

"Password":"9LHZEiA2AhKsAtM4yOOrEw==" 

} 

Sonuç  

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Hash 

String 

Oturum süresi boyunca erişim 

sağlanacak oturum anahtarıdır. 

 

Örnek Response:  

{ 

"success": true,  

"nessage": "",  

"content": 

{  

"hash": 

"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpX

VCJ9.eyJBdXRob3JpemF0aW9uIjoiQXV0aG9yaXplZCIsIkN1c3RvbWVyTm8iOiIxMzQ1MTcyMCIsIk5ld3NsZXR0ZXIi

OiJUcnVlIiwiSXNCbG9ja2VkIjoiRmFsc2UiLCJFbWFpbCI6IjEzNDUxNzIwIiwiVXNlcklkIjoiMTAxIiwiRGVuaXpiYW5rIjoi

VHJ1ZSIsIm5iZiI6MTY1MzQ4NjMxMCwiZXhwIjoxNjUzNTcyNzEwfQ.8PtF5zNa24bSr3ed-

BuqzpeWqbgxK2rLRXQReovoC2c"  

} 

} 

 

 

Oturum Yenileme 

 

Oturum yenileme fonksiyonudur. 

 

Http İsteği  

 

• 

POST /api/ SessionRefresh 

 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

 

İstek Parametresi  

 

Herhangi bir parametre almamaktadır. 

 

Sonuç  

 

Bool  değer  döner. 

 

 

Sembol Bilgisi 

 

Sembol ile ilgili bilgileri getirir. 

 

Http İsteği  

 

• 

POST /api/GetEquityInfo 

 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

symbol 

String 

Sembol Kodu 

 

Örnek Body: 

 

{"symbol":"TSKB"} 

 

Sonuç  

 

Parametre Adı 

Parametre Tipi 

Açıklama 

name 

String 

Sembol Adı 

flr 

String 

Taban Fiyat 

clg 

String 

Tavan Fiyat 

ask 

String 

Alış Fiyatı 

bid 

String 

Satış Fiyatı 

lst 

String 

Son Fiyat 

limit 

String 

İşlem Limiti 

min 

String 

 

max 

String 

 

step 

String 

 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content":{  

"name": "TSKB",  

"flr": "1.840",  

"clg": "2.240",  

"ask": "2.060",  

"bid": "2.050",  

"lst": "2.060",  

"limit": "0.00",  

"min": "",  

"max": "",  

"step": ""  

}  

} 

 

 

Alt Hesap Bilgileri 

 

Kullanıcıya ait alt hesap bilgilerini getirir. 

 

Http İsteği  

 

• 

POST /api/GetSubAccounts 

 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

 

İstek Parametresi  

 

Parametresi  bulunmamaktadır. 

 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Number 

String 

Alt Hesap Numarası 

TradeLimit 

String 

Alt Hesap İşlem Limiti 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content":  

[{  

"number": "100",  

"tradeLimit": "10000.00"  

},  

{  

"number": "100",  

"tradeLimit": "10000.00"  

}]  

} 

 

 

Hisse Portföy Bilgisi 

 

Kullanıcıya ait anlık portföy bilgilerini getirir. 

 

Http İsteği  

 

• 

POST /api/InstantPosition 

 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Subaccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{"Subaccount":""} 

 

 

Sonuç  

 

Parametre Adı 

Parametre Tipi 

Açıklama 

maliyet 

String 

Menkul kıymetin alış fiyatı 

totalstock 

String 

Menkul kıymetin Toplam Miktarı 

code 

String 

Enstrüman ismi 

profit 

String 

Menkul kıymetin birim fiyatı ile alış 

fiyatı farkından elde ettiği kazancı 

cost 

String 

 

unitprice 

String 

Menkul kıymetin birim fiyatı 

totalamount 

String 

Toplam satır bakiye TL değeri 

tlamaount 

String 

TL tutarı 

explanation 

String 

Portföyde bulunan menkul kıymetin 

açıklaması 

type 

String 

Overall kaleminin tipi 

total 

String 

 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content":  

[  

{  

"maliyet": "0",  

"totalstock": "0",  

"code": "TRY",  

"profit": "0",  

"cost": "0",  

"unitprice": "1",  

"totalamount": "",  

"tlamaount": "52.63",  

"explanation": "TRY",  

"type": "CA",  

"total": "0"  

},  

{  

"maliyet": "2.05",  

"totalstock": "1",  

"code": "TSKB",  

"profit": "0",  

"cost": "2.05",  

"unitprice": "2.05",  

"totalamount": "",  

"tlamaount": "2.05",  

"explanation": "TSKB",  

"type": "CH",  

"total": "0"  

}  

]  

} 

 

 

Viop Özeti 

 

Kullanıcıya ait Viop özet bilgilerini getirir. 

 

Http İsteği  

 

• 

POST /api/ViopCollateralInfo 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Subaccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{"Subaccount":""} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

sumcustody 

String 

Takastaki teminat 

sumorganization 

String 

Kurum teminatı 

sumcustodycalc 

String 

Çarpılmış hesaplanan kurum teminatı 

sumorganizationcalc 

String 

Çarpılmış hesaplanan kurum teminatı 

noncash 

String 

Takas nakit dışı teminat 

noncashorg 

String 

Takas nakit dışı kurum teminatı 

sumscanvalue 

String 

Scan değeri 

sumspreadvalue 

String 

Yayılma maliyeti 

sumshortoptionminimum 

String 

Kısa opt. Asgari teminatı 

scanrisk 

String 

Scan riski 

availablenetoption 

String 

Net opsiyon değeri 

waitingpremium 

String 

Bekleyen ödenecek prim 

deliverychange 

String 

Teslimat maliyeti 

maintanancerequirements 

String 

Sürdürme teminatı 

initialrequirements 

String 

Başlangıç teminatı 

requiredcollateral 

String 

Bulunması gereken teminat 

instantprofitloss 

String 

Anlık kar/zarar 

freecoll 

String 

Çekilebilir teminat 

usablecoll 

String 

Kullanılabilir teminat 

risklevel 

String 

Risk seviyesi 

custodymargincallamount 

String 

Margin call miktarı 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content":  

[  

{  

"sumcustody": "0",  

"sumorganization": "0",  

"sumcustodycalc": "0",  

"sumorganizationcalc": "0",  

"noncash": "0",  

"noncashorg": "0",  

"sumscanvalue": "0",  

"sumspreadvalue": "0",  

"sumshortoptionminimum": "0",  

"scanrisk": "0",  

"availablenetoption": "0",  

"waitingpremium": "0",  

"deliverychange": "0",  

"maintanancerequirements": "0",  

"initialrequirements": "0",  

"requiredcollateral": "0",  

"instantprofitloss": "0",  

"freecoll": "0", 

"usablecoll": "0",  

"risklevel": "0",  

"custodymargincallamount": "0" 

}  

]  

} 

 

 

Hisse Özeti 

 

Kullanıcıya ait Hisse özet bilgilerini getirir. 

 

Http İsteği  

 

• 

POST /api/RiskSimulation 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Subaccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{"Subaccount":""} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

t0 

String 

T Nakit Bakiyesi 

t1 

String 

T+1 Nakit Bakiyesi 

t2 

String 

T+2 Nakit Bakiyesi 

t0stock 

String 

 

t1stock 

String 

 

t2stock 

String 

 

t0equity 

String 

T Hisse Portföy Değeri 

t1equity 

String 

T+1 Hisse Portföy Değeri 

t2equity 

String 

T+2 Hisse Portföy Değeri 

t0overall 

String 

T Overall Değeri Nakit Dahil 

t1overall 

String 

T+1 Overall Değeri Nakit Dahil 

t2overall 

String 

T+2 Overall Değeri Nakit Dahil 

t0capitalrate 

String 

T Özkaynak Oranı 

t1capitalrate 

String 

T+1 Özkaynak Oranı 

t2capitalrate 

String 

T+2 Özkaynak Oranı 

netoverall 

String 

Nakit Hariç Overall 

shortfalllimit 

String 

Açığa satış sözleşmesi olan 

müşteriler için kullanılabilir açığa 

satış bakiyesi 

credit0 

String 

T Nakit Bakiyesi 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content":  

[  

{  

"t0": "0",  

"t1": "0",  

"t2": "0",  

"t0stock": "0",  

"t1stock": "0",  

"t2stock": "0",  

"t0equity": "0",  

"t1equity": "0",  

"t2equity": "0",  

"t0overall": "0",  

"t1overall": "0",  

"t2overall": "0",  

"t0capitalrate": "0",  

"t1capitalrate": "0",  

"t2capitalrate": "0",  

"netoverall": "0",  

"shortfalllimit": "0",  

"credit0": "0"  

}  

]  

} 

 

 

Hisse Günlük İşlemler 

 

Kullanıcıya ait günlük işlem kayıtlarını getirir. 

 

Http İsteği  

 

• 

POST /api/TodaysTransaction 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Subaccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{"Subaccount":""} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

atpref 

String 

Referans Numarası 

ticker 

String 

Hisse Senedi İsmi 

buysell 

String 

İşlemin Cinsi (Alış, Satış) 

ordersize 

String 

Emir Miktarı 

remainingsize 

String 

Emrin BIST’ te henüz karşılanmamış 

ve kalan bölümü bu sahada belirtilir. 

price 

String 

Emrin ortalama gerçekleşme fiyatını 

belirtir. 

amount 

String 

Gerçekleşen kısım ile ilgili 

müşterinin hesabından çekilecek 

veya hesabına yatırılacak meblağ bu 

sahada bulunmaktadır. 

transactiontime 

String 

Emrin giriş tarihini belirtir. Kısa tarih 

formatındadır. 

timetransaction 

String 

Emrin girildiği tarih uzun tarih 

formatındadır. 

valor 

String 

Emrin geçerliliğinin başladığı seans 

tarihini belirtir. Kısa tarih 

formatındadır. 

status 

String 

Emrin değiştirilebilme durumu 

bilgilerini içerir; Emir Silme, 

İyileştirme ve valör iptali 

işlemlerinin yapılıp yapılamayacağı 

bu bilgilerden anlaşılır. 5 haneden 

oluşan bir “string” değerdir. Her bir 

karakter “0” (“Mümkün Değil”) veya 

“1” (“Mümkün”) olabilir. Soldan 

itibaren birinci değer emrin silinip 

silinemeyeceğini belirtir. İkinci ve 

üçüncü değerler fiyat iyilestirme ve 

emir bölme işlemlerinin yapılıp 

yapılamayacağını belirtir. Sonraki 

değer ise emrin geçerlilik süresinin 

iptal edilip edilemeyeceğini belirtir. 

En son değer emrin kötüleştirilip 

kötüleştirilemiyeceğini belirtir. 

waitingprice 

String 

Emrin bekleyen kısmının fiyatını 

belirtir. Emir fiyatı olarak bu alan 

kullanılmalıdır. 

description 

String 

Emir durumu bilgisini belirtir; 

o 

İletildi 

o 

Silindi 

o 

İyileştirme Talebi Alındı 

o 

İyileştirildi 

o 

Silme Talebi Alındı 

o 

İyileştirme Reddedildi 

o 

Emir Reddedildi 

o 

Silme Reddedildi 

o 

KIE Emri Silindi 

o 

KPY Emri Silindi 

o 

Gerçekleşti 

o 

Kısmi Gerçekleşti 

Emir Bekliyor 

transactionId 

String 

GTP’de tutulan referansı belirtir. 

İşlemler GTP’ye bu referans 

gönderilir. GTP emri bu id ile 

tanır. GTP’de unique olarak 

tutulur. 

equityStatusDescription 

String 

Ekranda emirleri gruplayabilmek 

amaçıyla gönderilen özel bir alandır. 

o 

WAITING: Bekleyen Emirler 

o 

DONE: Gerçekleşen Emirler 

o 

PARTIAL: Kısmi Gerçekleşen 

Emirler 

o 

IMPROVE_DEMAND: Emir 

iyileştirme talebi alındı 

o 

DELETE_DEMAND: Emir 

silme talebi alındı 

o 

DELETED: Gerçekleşmesi 

olmayan silinmiş emirler, borsadan 

red almış emirler. 

shortfall 

String 

Açığa satış 

timeinforce 

String 

Emrin geçerlilik süresini belirtir. 

Emir girişinde kullanılan değerler 

geri dönülür. 

fillunit 

String 

Gerçekleşme adet bilgisini verir. 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content":  

[  

{  

"atpref": "0013O2",  

"ticker": "TSKB",  

"buysell": "Alış",  

"ordersize": "1",  

"remainingsize": "0",  

"price": "2.050000",  

"amount": "2.050000",  

"transactiontime": "27.05.2022 00:00:00",  

"timetransaction": "27.05.2022 11:47:32",  

"valor": "27.05.2022",  

"status": "00000",  

"waitingprice": "2.050000",  

"description": "Gerçekleşti",  

"transactionId": "0000-291B5D-IET",  

"equityStatusDescription": "DONE",  

"shortfall": "0",  

"timeinforce": "",  

"fillunit": "1"  

}  

]  

} 

 

 

Viop Portföy Bilgisi 

 

Müşterinin pozisyon ve kar zarar bilgilerini içeren overall bilgisini getirir. 

Http İsteği  

 

• 

POST /api/ViopCustomerOverall 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Subaccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{"Subaccount":""} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

contract 

String 

Sözleşme Adı 

contractname 

String 

Sözleşme Adı 

shortlong 

String 

Uzun, Kısa 

units 

String 

Adet 

putcall 

String 

Put/Call Bilgisi 

shortbalance 

String 

Kısa Adet 

longbalance 

String 

Uzun Adet 

openpositiontotal 

String 

Toplam Açık Pozisyon 

exerciseunits 

String 

Fiziki Kullanım Miktarı 

waitingexerciseunits 

String 

Fiziki Kullanım Bekleten Miktar 

unitnominal 

String 

Ümit Nominal 

totalcost 

String 

Toplam Maliyet 

profit 

String 

Opsiyon kullanımında elde edilecek 

Kar/Zarar 

profitloss 

String 

Muhasebeleşmiş Kar/Zarar 

dailyprofitloss 

String 

Adet * (uzlaşma - önceki uzlaşma) * 

birim nominal (pozisyon kar-zararı) 

(Futures) 

potprofit 

String 

Pozisyon maliyetine göre kar/zarar 

fininstid 

String 

 

 

 

 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content": [  

{  

"contract": "-",  

"contractname": "-",  

"shortlong": "-",  

"units": "-",  

"putcall": "-",  

"shortbalance": "-",  

"longbalance": "-",  

"openpositiontotal": "-",  

"exerciseunits": "-",  

"waitingexerciseunits": "-",  

"unitnominal": "-",  

"totalcost": "-",  

"profit": "-",  

"profitloss": "-",  

"dailyprofitloss": "-",  

"potprofit": "-",  

"fininstid": "-"  

}  

]  

} 

 

 

Viop Günlük İşlemler 

 

Müşterinin pozisyon ve kar zarar bilgilerini içeren overall bilgisini getirir. 

Http İsteği  

 

• 

POST /api/ViopCustomerTransactions 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Subaccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{"Subaccount":""} 

Sonuç  

 

Parametre Adı 

Parametre Tipi 

Açıklama 

contract 

String 

Sözleşme adı 

shortlong 

String 

Uzun kısa (Alış\Satış) sözleşme 

bilgisi 

units 

String 

Emir miktarı 

leftunits 

String 

Kalan miktar 

price 

String 

Emir fiyatı 

transactionid 

String 

Emir ID’ si 

transactiondate 

String 

Emir tarihi 

transactionenddate 

String 

Emir bitiş tarihi 

transactiondatetype 

String 

Emir gün tipi (DAY, DTD, SNS, vs.) 

transactionunitnominal 

String 

Emir nominal değeri 

transactionunit 

String 

Gerçekleşen adet 

trexid 

String 

Emir referans değeri 

description 

String 

Emir açıklaması (API’ de hataya 

düşmesi durumunda) 

- 

Gerçekleşti 

- 

Kısmen gerçekleşti 

- 

İletildi 

- 

Bekliyor 

- 

İptal 

ordertime 

String 

Emir gerçekleşme zamanı 

(dd.mm.yyyy hh:MM:SS) 

validity 

String 

Emir gün tipi 

fininstid 

String 

Alt sözleşme ID’ si 

ordertype 

String 

Emir tipi 

pricetype 

String 

Emir fiyat tipi açıklaması (Limitli, 

Kalanı Pasife Yaz, vs.) 

pricetypename 

String 

Emir fiyat kodu (LMT, KPY vs.) 

info 

String 

Emir Durumu (Bekliyor, Gerçekleşti, 

İptal, Hata, Kısmi Gerçekleşti, 

İletildi) 

timeinforce 

String 

Emir Süresi 

realizedunits 

String 

Emir gerçekleşen miktarı 

priceaverage 

String 

Ortalama gerçekleşme fiyatı 

transstatusname 

String 

Emir durum bilgisi 

-ACTIVE Aktif 

-IMPROVE_DEMAND İyileştirilen Emir 

-IMPROVE_ORDER  İyileştirilecek Emir 

-READED_BY_DISC_ORDER 

Disket emir 

tarafından okunmuş kayıtlar. 

-CORRECT_DEMAND 

Update edilmek 

istenen kayıtlar. 

-CANCEL_DEMAND 

İptal edilmek 

istenen kayıtlar. 

-CANCEL_ORDER 

İptal edilen kayıtlar. 

-CORRECT_ORDER 

Update edilen 

kayıtlar. 

-API_ERROR 

API `den geri döndü 

-API_IMPROVE_ERROR Emir iyileştirmede 

API Hatası alındı 

-API_CANCEL_ERROR 

Emir iptalinde API 

Hatası alındı 

-PARTIAL_FILL Parçalı Gerçekleşme 

-FILLED  Gerçekleşme 

-DONE    Done For Day 

-STOPPED 

Durmuş 

-REJECTED 

Reddedildi 

-PENDING_NEW 

Onay bekliyor 

-CALCULATED 

Calculated 

-EXPIRED 

Süresi Dolmuş 

-ACCEPT_BIDDING 

Teklif Kabul Edilmiş 

-SUSPENDED 

Geçici Olarak Durmuş 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content": [  

{  

"contract": "-",  

"contractname": "-",  

"shortlong": "-",  

"units": "-",  

"putcall": "-",  

"shortbalance": "-",  

"longbalance": "-",  

"openpositiontotal": "-",  

"exerciseunits": "-",  

"waitingexerciseunits": "-",  

"unitnominal": "-",  

"totalcost": "-",  

"profit": "-",  

"profitloss": "-",  

"dailyprofitloss": "-",  

"potprofit": "-",  

"fininstid": "-"  

}  

]  

} 

 

 

Emir Gönderim 

 

Alım/satım emrini iletir. 

Http İsteği  

 

• 

POST /api/SendOrder 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi  

 

Parametre Adı 

Parametre Tipi 

Açıklama 

symbol 

String 

Sembol Kodu 

direction 

String 

İşlem Yönü: BUY / SELL (Alış/Satış) 

pricetype 

String 

Emir Tipi: piyasa/limit 

price 

String 

Emir tipi limit ise fiyat girilmelidir. 

(1.98 şeklinde girilmelidir.) 

lot 

String 

Emir Adeti 

sms 

Bool 

Sms Gönderim 

email 

Bool 

Email Gönderim 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"symbol":"TSKB",  

"direction":"BUY",  

"pricetype":"limit",  

"price":"2.01",  

"lot":"1",  

"sms":true,  

"email":false,  

"Subaccount":""  

} 

Sonuç  

 

Emir doğru bir şekilde iletilmiş ise sistemden String olarak emir referans numarası dönmektedir. Aşağıdaki işaretli 

numara ile emrinizi düzenleyebilir silebilirsiniz. 

Örnek Response: 

{  

"success": true,  

"message": "",  

"content": "Referans Numaranız: 001VEV;0000-2923NR-IET - HISSEOK"  

} 

 

 

Emir İyileştirme 

 

Gönderilen ve açık olan emiri iyileştirir. 

Http İsteği  

 

• 

POST /api/ModifyOrder 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

id 

String 

Emrin ID’ si 

price 

String 

Düzeltilecek Fiyat 

lot 

String 

Lot Miktarı (Viop emri ise 

girilmelidir.) 

viop 

Bool 

Emrin Viop emri olduğunu belirtir. 

“Viop emri ise true olmalıdır.” 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"id":"001VEV",  

"price":"2.04",  

"lot":"0",  

"viop":false,  

"Subaccount":""  

} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

message 

String 

Emrin iletimi hakkında bilgi verir. 

duration 

String 

 

 

Örnek Response: 

{  

"success": true,  

"message": "IYILESOK",  

"content": {  

"message": "IYILESOK",  

"duration": "-"  

}  

} 

 

 

Hisse Emri İptal Etme 

 

Gönderilen ve açık olan hisse emrini iptal eder. 

Http İsteği  

 

• 

POST /api/DeleteOrder 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

id 

String 

Emrin ID’ si 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"id":"001VEV",  

"subAccount":""  

} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

message 

String 

Emrin iletimi hakkında bilgi verir. 

duration 

String 

 

 

Örnek Response: 

{  

"success": true,  

"message": "Success",  

"content": {  

"message": "Success",  

"duration": "-"  

}  

} 

 

 

VIOP Emri İptal Etme 

 

Gönderilen ve açık olan viop emrini iptal eder. 

Http İsteği  

 

• 

POST /api/DeleteOrderViop 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

id 

String 

Emrin ID’ si 

adet 

String 

İptal edilecek adet 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"id":"001VEV",  

"adet":"1",  

"subAccount":""  

} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

message 

String 

Emrin iletimi hakkında bilgi verir. 

duration 

String 

 

 

Örnek Response: 

{  

"success": true,  

"message": "Canceled",  

"content": {  

"message": "Canceled",  

"duration": "-"  

}  

} 

 

 

Hisse Emir Tarihçesi 

Gönderilen hisse emrinin tarihçesini görüntüler. 

Http İsteği  

 

• 

POST /api/GetEquityOrderHistory 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

transactionId 

String 

Emrin ID’ si 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"transactionId":"001VEV",  

"subAccount":""  

} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

TransactionExtId 

String 

İşlem ID’si 

Equity 

String 

Hisse İsmi 

DebitCredit 

String 

Alış/Satış 

Units 

String 

Adet 

Price 

String 

Fiyat 

Created 

String 

Tarih 

Status 

String 

Durumu (Bekliyor,Kabul 

Edildi,Reddedildi) 

TransTypeId 

String 

Durum Tipi (Yeni Emir Talebi, Emir İptal 

Talebi, Değiştirme Talebi) 

 

Örnek Response: 

{  

"success": true,  

"message": "Canceled",  

"content": {  

"transactionExtId": "İşlem ID’si",  

"equity": "Hisse İsmi", 

"debitCredit": "Alış/Satış",  

"units": "Adet", 

"price": "Fiyat", 

"created": "Tarih", 

"status": "Durumu", 

"transTypeId": "Durum Tipi", 

} } 

Viop Emir Tarihçesi 

Gönderilen viop emrinin tarihçesini görüntüler. 

Http İsteği  

 

• 

POST /api/GetViopOrderHistory 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

transactionId 

String 

Emrin ID’ si 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"transactionId":"001VEV",  

"subAccount":""  

} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

TransactionExtId 

String 

İşlem ID’si 

Contract 

String 

Sözleşme 

ShortLong 

String 

Emir Yönü(Short,Long) 

Price 

String 

Fiyat 

Units 

String 

Adet 

SentTime 

String 

Tarih 

ResultType 

String 

Durumu (New Order, Completed vs.) 

Message 

String 

   Mesaj 

 

Örnek Response: 

{  

"success": true,  

"message": "Canceled",  

"content": {  

"transactionExtId": "İşlem ID’si",  

"contract": "Sözleşme", 

"shortLong": "Short/Long",  

"units": "Adet", 

"price": "Fiyat", 

"sentTime": "Tarih", 

"resultType": "Durumu", 

"message": "Mesaj", 

} } 

 

 

Hesap Ekstresi 

Kullanıcıya ait ilgili tarihler arasındaki hesap ekstresini verir. 

Http İsteği  

 

• 

POST /api/AccountExtre 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

start 

DateTime 

Başlangıç Tarihi 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"start":2023-07-01 00:00:00,  

"end":2023-07-31 00:00:00,  

"subAccount":""  

} 

Sonuç 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

accountextre 

List<AccountExtre> 

Hisse Ekstre 

viopextre 

List<ViopAccountStatement> 

Viop Ekstre 

 

AccountExtre: 

Parametre Adı 

Parametre Tipi 

Açıklama 

transdate 

string 

İşlemin muhasebe tarihini 

explanation 

string 

İşlemin açıklamasını 

debit 

string 

İşlem ile ilgili borç miktarını 

credit 

string 

İşlem ile ilgili alacak miktarını 

balance 

string 

İşlem sonrasındaki hesabın bakiyesini 

valuedate 

string 

İşlemin valör tarih ve saatini 

 

ViopAccountStatement: 

Parametre Adı 

Parametre Tipi 

Açıklama 

shortlong 

string 

Uzun kısa (Alış\Satış) sözleşme bilgisi 

transactiondate 

string 

Emir zamanı 

contract 

string 

İşlem yapılan sözleşme adı 

credit 

string 

Alınan miktar 

debit 

string 

Satılan miktar 

units 

string 

Sözleşme adedi 

price 

string 

Sözleşme fiyatı 

balance 

string 

Hesap Bakiyesi 

currency 

string 

Para birimi 

 

Örnek Response: 

{  

"success": true,  

"message": "Canceled",  

"content": {  

"accountextre": [{ 

"transdate": "",  

"explanation ": "",  

"debit": "",  

"credit": "",  

"balance": "",  

"valuedate": "",  

}], 

"viopextre": [{ 

"shortlong": "",  

"transactiondate": "",  

"contract": "",  

"credit": "",  

"debit": "",  

"units": "",  

"price": "",  

"balance": "",  

"currency": "",  

 

}] 

} } 

 

 

 

Nakit Bakiye 

T0, T+1, T+2 nakit bayileri getirir. 

Http İsteği  

 

• 

POST /api/CashFlow 

Http Headers  

 

Content-Type: application/json APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

İstek Parametresi 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

subAccount 

String 

Alt Hesap Numarası 

“Boş gönderilebilir. Boş gönderilir 

ise 

Aktif Hesap Bilgilerini getirir.” 

 

Örnek Body: 

{  

"subAccount":""  

} 

Sonuç  

 

Parametre Adı 

Parametre Tipi 

Açıklama 

t0 

String 

T+0 anındaki nakit bakiye 

t1 

String 

T+1 anındaki nakit bakiye 

t2 

String 

T+2 anındaki nakit bakiye 

 

Örnek Response: 

{  

"success": true,  

"message": "Canceled",  

"content": {  

"t0": "",  

"t1": "", 

"t2": "" 

} } 

 

 

WebSoket Protokolü (wss) 

 

Canlı veya gecikmeli veri görüntülemenizi sağlar. 

Http İsteği  

 

• 

GET /ws 

Http Headers  

 

APIKEY: Başvuru Sonucu Alınan APIKEY 

Authorization: Kullanıcı Girişi Oturum Alma işleminden dönen Hash değeri Checker: Her istek için oluşturulan 

imzadır. 

Mesaj Gönderimi  

 

1. HeartBeat 

 

Aşağıdaki şekilde Json String gönderilir. Type= H olmalıdır. Token değeri = Authorization 

{"Type":"H","Token":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1

NiIsInR5 

cCI6IkpXVCJ9.eyJBdXRob3JpemF0aW9uIjoiQXV0aG9yaXplZCIsIkN1c3RvbWVyTm8iOiIxMzQ1MTcyMCIsIk5ld3NsZXR0

ZXIiOiJU 

cnVlIiwiSXNCbG9ja2VkIjoiRmFsc2UiLCJFbWFpbCI6IjEzNDUxNzIwIiwiVXNlcklkIjoiMTAxIiwiRGVuaXpiYW5rIjoiVHJ1ZSIsI 

m5iZiI6MTY1MzkyMDg2NiwiZXhwIjoxNjU0MDA3MjY2fQ.kzkSYQOnkA9Qn8qTiV_Fq8IvqXKsQ3m-QuMv6Kjqkdw"} 

2. T Paketi Abone Olma 

 

Aşağıdaki şekilde Json String gönderilir. Type= T olmalıdır.  Token değeri = Authorization , Symbols= List<string>() 

Symbols yerine T paketinde gelmesi istenilen semboller liste şeklinde yazılır. Bütün Sembollerin gelmesi için "ALL" 

yazılması gerekmektedir. 

{"Type":"T","Token":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1

NiIsInR5 

cCI6IkpXVCJ9.eyJBdXRob3JpemF0aW9uIjoiQXV0aG9yaXplZCIsIkN1c3RvbWVyTm8iOiIxMzQ1MTcyMCIsIk5ld3NsZXR0

ZXIiOiJU 

cnVlIiwiSXNCbG9ja2VkIjoiRmFsc2UiLCJFbWFpbCI6IjEzNDUxNzIwIiwiVXNlcklkIjoiMTAxIiwiRGVuaXpiYW5rIjoiVHJ1ZSIsI 

m5iZiI6MTY1MzkyMDg2NiwiZXhwIjoxNjU0MDA3MjY2fQ.kzkSYQOnkA9Qn8qTiV_Fq8IvqXKsQ3m-

QuMv6Kjqkdw","Symbols":["GARAN","TSKB"]} 

 

 

 

3. D Paketi Abone Olma 

 

Aşağıdaki şekilde Json String gönderilir. Type= D olmalıdır.  Token değeri = Authorization , Symbols= List<string>() 

Symbols yerine D paketinde gelmesi istenilen semboller liste şeklinde yazılır. Bütün Sembollerin gelmesi için "ALL" 

yazılması gerekmektedir. 

{"Type":"D","Token":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1

NiIsInR5 

cCI6IkpXVCJ9.eyJBdXRob3JpemF0aW9uIjoiQXV0aG9yaXplZCIsIkN1c3RvbWVyTm8iOiIxMzQ1MTcyMCIsIk5ld3NsZXR0

ZXIiOiJU 

cnVlIiwiSXNCbG9ja2VkIjoiRmFsc2UiLCJFbWFpbCI6IjEzNDUxNzIwIiwiVXNlcklkIjoiMTAxIiwiRGVuaXpiYW5rIjoiVHJ1ZSIsI 

m5iZiI6MTY1MzkyMDg2NiwiZXhwIjoxNjU0MDA3MjY2fQ.kzkSYQOnkA9Qn8qTiV_Fq8IvqXKsQ3m-

QuMv6Kjqkdw","Symbols":["GARAN"]} 

 

 

Sonuç  

Akışta aşağıdaki şekilde model gelmektedir. 

 

Parametre Adı 

Parametre Tipi 

Açıklama 

Type 

String 

T: Tick Paketi (Fiyat) 

D: Depth Paketi (Derinlik) 

O: Emir Statüsü 

Content 

dynamic 

Açıklamaya Göre Model 

Değişmektedir. 

 

Örnek Response T Type: 

{  

"Type": "T",  

"Content": {  

"Symbol": "VERTU",  

"Market": "IMKBH",  

"Price": 22.78,  

"Change": 0.1,  

"Ask": 22.78,  

"Bid": 22.8,  

"Date": "2022-05-30T11:51:59+03:00",  

"ChangePercentage": 0.44,  

"High": 22.9,  

"Low": 22.78,  

"TradeQuantity": 410.0,  

"Direction": "S",  

"RefPrice": 22.7,  

"BalancePrice": 0.0,  

"BalanceAmount": 0.0,  

"Buying": "XXXXX",  

"Selling": "XXXXX"  

} }   

 

Örnek Response D Type: 

{  

"Type": "D",  

"Content": {  

"Symbol": "F_HEKTS0522",  

"Market": "VIP",  

"Direction": "B",  

"Row": 20,  

"Quantity": 3,  

"Price": 29.49,  

"OrderCount": 1,  

"Date": "2022-05-30T17:25:05.7561532+03:00"  

} } 

 

Örnek Response O Type: 

{  

"Type": "O",  

"Content": {  

"Id": "xwewr",  

"Date": "2022-05-30T11:51:59+03:00",  

"Direction": "BUY",  

"Symbol": "GARAN",  

"Lot": 1,  

"PriceType": "Market",  

"Price": 22.78,  

"Comment": "Açıklama",  

"Status": "Waiting",  

"Channel": "",  

}} 




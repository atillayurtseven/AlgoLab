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



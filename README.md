
# AlgoLab Python Wrapper

## Genel Bakış
Bu proje, AlgoLab API'si için bir Python wrapper'ıdır. `algolab.py` ve `algolab_socket.py` modülleri aracılığıyla AlgoLab API'sine erişim sağlar. Kullanıcıların AlgoLab platformundaki verilere programatik olarak erişmelerini ve işlemler yapmalarını kolaylaştırır.

## Kurulum
Projeyi kullanmak için, bu repoyu klonlayın ve gerekli bağımlılıkları kurun.

```
git clone [repo-url]
cd [repo-directory]
pip install -r requirements.txt
```

## Kullanım
API'yi kullanmak için, öncelikle `config.py` dosyasında gerekli yapılandırmaları yapın. Daha sonra `algolab.py` ve `algolab_socket.py` modüllerini projenizde import ederek kullanabilirsiniz.

Örnek kullanım:

```python
from algolab import AlgoLab
from algolab_socket import AlgoLabSocket

# API ile etkileşim
algolab = AlgoLab(api_key="your_api_key", username="your_username", password="your_password")
response = algolab.your_method()

# Soket ile etkileşim
socket = AlgoLabSocket(api_key="your_api_key", hash="your_hash")
socket.connect()
```

## Yapılandırma
`config.py` dosyası, API ve soket bağlantıları için temel yapılandırmaları içerir. API'nin hostname'i ve diğer sabitler bu dosyada tanımlanır.

## Bağımlılıklar
Bu wrapper'ın çalışması için gerekli bağımlılıklar `requirements.txt` dosyasında listelenmelidir.

## AlgoLab Link
https://algolab.com.tr/

## Lisans ve Yazar Bilgisi
Bu proje MIT altında yayınlanmıştır.
Atilla Yurtseven
---

Bu dokümantasyon, projenin temel kullanımını ve yapılandırmasını anlatmaktadır. Daha detaylı bilgi ve örnekler için, lütfen kod içindeki yorumları inceleyin.

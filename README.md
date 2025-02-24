# 📝 WordPress Blog ve Veri Yönetimi Projesi

Bu proje, **WordPress API**, **PostgreSQL**, **MongoDB**, **Redis** ve **Docker** kullanarak bir blog yönetim sistemini kapsar.  
Proje, blog yazıları oluşturma/güncelleme, veri yükleme ve çoklu veritabanı yönetimi gibi işlemleri otomatize eden bir yapıya sahiptir.

---

## 🚀 Özellikler

- **WordPress API** ile blog yazıları oluşturma ve güncelleme
- **PostgreSQL** ve **MongoDB** ile veri yönetimi
- **Redis** ile veri önbellekleme
- **Docker Compose** kullanılarak mikro servislerin yönetimi
- **Tam Otomatik Başlatma** ve sağlık kontrolleri
- **AWS Üzerinde Çalıştırılabilir Mimari**
- **Apache Web Server ile WordPress Entegrasyonu**

---

## 📦 Kullanılan Teknolojiler

| Teknoloji       | Açıklama |
|----------------|----------|
| Python 3.9     | Veri işlemleri ve API çağrıları |
| PostgreSQL     | Kullanıcı verilerini saklamak için |
| MongoDB        | Alternatif NoSQL veritabanı |
| Redis          | Hızlı önbellekleme sistemi |
| WordPress      | Blog yönetim sistemi |
| Apache         | HTTP sunucu |
| MySQL          | WordPress veritabanı |
| Docker & Compose | Konteyner yönetimi |
| Bash Script    | Otomatik başlatma ve servis kontrolleri |

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi çalıştırmadan önce, aşağıdaki adımları takip etmelisiniz:

### 1️⃣ Bağımlılıkları Yükleyin
Sisteminizde **Docker** ve **Docker Compose** kurulu olmalıdır. Eğer eksikse şu komutlarla yükleyebilirsiniz:

```sh
# Docker yükleme (Ubuntu)
sudo apt update && sudo apt install docker docker-compose -y
```

### 2️⃣ Projeyi Klonlayın
```sh
git clone https://github.com/kullanici/proje-repo.git
cd proje-repo
```

### 3️⃣ Projeyi Docker ile Başlatın
```sh
bash startup.sh
```

Bu komut aşağıdaki adımları gerçekleştirir:
✅ Docker servislerini başlatır  
✅ WordPress’in API’sinin erişilebilir olup olmadığını kontrol eder  
✅ Veri yükleme işlemini gerçekleştirir  

### 4️⃣ WordPress Paneline Erişim
- **Adres:** [http://localhost:8080](http://localhost:8080)
- **Kullanıcı Adı:** `admin`
- **Şifre:** `admin_password`

### 5️⃣ Veritabanı Bağlantıları
- **PostgreSQL** `localhost:5432` (Kullanıcı: `myuser`, Şifre: `mypassword`)
- **MongoDB** `localhost:27017`
- **Redis** `localhost:6379`

---

## 🏗️ Servislerin Açıklaması

| Servis | Açıklama |
|--------|----------|
| `wordpress` | WordPress blog yönetim sistemi |
| `mysql-db` | WordPress için MySQL veritabanı |
| `apache` | HTTP sunucu |
| `postgresql` | Kullanıcı ve veri yönetimi için PostgreSQL |
| `mongo` | Alternatif NoSQL veritabanı |
| `redis` | Hızlı önbellekleme için Redis |
| `data_loader` | PostgreSQL ve MongoDB'ye veri yükleyen servis |
| `wp_updater` | WordPress’te yazı ekleme ve güncelleme yapan servis |

---

## 📜 API Kullanımı

### 📌 Blog Yazısı Oluşturma

```sh
curl -X POST "http://localhost:8080/wp-json/wp/v2/posts"   -u admin:admin_password   -H "Content-Type: application/json"   -d '{"title":"Yeni Yazı", "content":"Bu bir test yazısıdır.", "status":"publish"}'
```

### ✏️ Blog Yazısı Güncelleme

```sh
curl -X PUT "http://localhost:8080/wp-json/wp/v2/posts/1"   -u admin:admin_password   -H "Content-Type: application/json"   -d '{"title":"Güncellenmiş Yazı", "content":"Bu yazı güncellenmiştir!", "status":"publish"}'
```

---

## 🌍 AWS Üzerinde Çalıştırma

Eğer **AWS EC2** üzerinde çalıştırmak istiyorsanız:
1. EC2 üzerine **Ubuntu 22.04** kurun.
2. Docker ve Docker Compose yükleyin.
3. Projeyi klonlayıp `startup.sh` çalıştırın.
4. AWS Güvenlik Gruplarından **80, 8080, 3306, 5432, 27017, 6379** portlarını açın.
5. WordPress'e erişmek için `http://ec2-kendi-ip-adresin:8080` adresini kullanın.

---

## 📌 MİMARİ ÇİZİM (EXCALIDRAW)

Aşağıdaki Excalidraw mimarisinde, projenin **AWS Sybelle ortamında nasıl çalışacağı** gösterilmektedir:

- **EC2** sanal makinesi üzerine Docker kurulu
- **WordPress + MySQL** ayrı konteynerlerde çalışıyor
- **PostgreSQL + MongoDB** veritabanı yönetimi sağlıyor
- **Redis** önbellekleme için kullanılıyor
- **Python Servisleri** veri yükleme ve blog güncelleme işlemleri yapıyor

⏳ **Bu çizimi oluşturmak için Excalidraw’ı açıp gerekli bileşenleri yerleştireceğiz.**  

---

## 🎯 Sonuç

Bu proje, **WordPress yönetimi**, **PostgreSQL/MongoDB veri yönetimi**, **Redis ile önbellekleme**, **Docker ile ölçeklenebilirlik** gibi birçok modern çözümü içermektedir.  

🔗 **Geliştirme süreciyle ilgili katkıda bulunmak için PR gönderebilirsiniz!**

📌 **Lisans:** MIT  
📌 **Geliştirici:** [Utku Kadir Somer](https://github.com/utkuks-ce)  
📌 **İletişim:** `utkuks.ce@gmail.com`

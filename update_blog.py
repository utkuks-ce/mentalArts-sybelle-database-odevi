import requests

# WordPress API bilgileri
WORDPRESS_URL = "http://wordpress:80/wp-json/wp/v2/posts/1"  # WordPress konteynerine iç ağdan bağlanıyoruz
USERNAME = "admin"
PASSWORD = "admin_password"

# Güncellenecek veri
data = {
    "title": "Güncellenmiş Blog Yazısı",
    "content": "Bu blog yazısı güncellendi!",
    "status": "publish"
}

# Güncelleme isteği gönder
try:
    response = requests.put(WORDPRESS_URL, json=data, auth=(USERNAME, PASSWORD))

    if response.status_code == 200:
        print("✅ Blog yazısı başarıyla güncellendi!")
    else:
        print(f"⚠️ Hata: {response.status_code}, {response.text}")

except requests.exceptions.RequestException as e:
    print(f"❌ HTTP isteği başarısız oldu: {e}")


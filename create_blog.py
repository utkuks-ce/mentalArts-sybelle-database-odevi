import requests

# WordPress API bilgileri
WORDPRESS_URL = "http://wordpress/wp-json/wp/v2/posts"  # Düzeltildi
USERNAME = "admin"
PASSWORD = "admin_password"

# Yeni blog yazısı oluşturma
data = {
    "title": "İlk Blog Yazısı",
    "content": "Bu bir test blog yazısıdır.",
    "status": "publish"
}

# HTTP isteği gönderme
response = requests.post(WORDPRESS_URL, json=data, auth=(USERNAME, PASSWORD))

# Yanıtı ekrana yazdırma
if response.status_code == 201:
    print("Blog yazısı başarıyla oluşturuldu!")
else:
    print(f"Hata: {response.status_code}, {response.text}")


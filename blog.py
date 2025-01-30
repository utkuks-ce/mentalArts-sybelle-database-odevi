import requests

WORDPRESS_URL = "http://localhost:8080/wp-json/wp/v2/posts/1"  # İlk postu değiştireceğiz
USERNAME = "admin"
PASSWORD = "your_application_password"  # WordPress uygulama şifreni alman lazım!

# Güncellenecek içerik
data = {
    "title": "Güncellenmiş Başlık",
    "content": "Bu yazı Docker Compose kullanılarak güncellendi!",
    "status": "publish"
}

# WordPress REST API'ye kimlik doğrulama ile istek at
response = requests.post(WORDPRESS_URL, json=data, auth=(USERNAME, PASSWORD))

if response.status_code == 200:
    print("Blog yazısı başarıyla güncellendi!")
else:
    print(f"Bir hata oluştu: {response.text}")


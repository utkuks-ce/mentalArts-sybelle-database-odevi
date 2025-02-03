# WordPress blog yazısı oluşturmak ve güncellemek için temel Python imajı
FROM python:3.9-slim

WORKDIR /app

# Gerekli bağımlılıkları yükle
RUN pip install requests

# Script dosyalarını kopyala
COPY create_blog.py create_blog.py
COPY update_blog.py update_blog.py

# Varsayılan komut
CMD ["python", "create_blog.py"]


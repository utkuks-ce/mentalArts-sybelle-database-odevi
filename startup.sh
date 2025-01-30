#!/bin/bash

echo "📢 Docker Compose 1 başlatılıyor..."
docker-compose -f docker-compose.yml up -d

echo "✅ WordPress çalışıyor mu kontrol ediliyor..."
sleep 10  # Servislerin ayağa kalkmasını bekliyoruz

# Eğer WordPress çalışıyorsa Docker Compose 2'yi başlat
if docker ps | grep -q "wordpress"; then
    echo "📢 Docker Compose 2 başlatılıyor..."
    docker-compose -f docker-compose-2.yml up -d
else
    echo "❌ WordPress çalışmadı, Docker Compose 2 başlatılmadı!"
fi


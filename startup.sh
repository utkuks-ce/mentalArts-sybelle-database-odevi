#!/bin/bash

echo "Docker Compose 1 başlatılıyor..."
docker compose -f docker-compose.yml up -d
sleep 10  

echo "WordPress'in tam olarak hazır olmasını bekliyoruz..."
until $(curl --output /dev/null --silent --head --fail http://localhost:8080/wp-json/wp/v2/posts); do
    printf '.'
    sleep 5
done
echo "WordPress API artık çalışıyor!"

echo "Docker Compose 2 başlatılıyor..."
docker compose -f docker-compose.yml -f docker-compose-2.yml up -d
sleep 10  

echo "Veritabanları hazır!"
echo "veritabanına ilk giriş yapılıyor"

echo "data_loader başlatılıyor..."
docker start data_loader || echo "data_loader çalıştırılamadı!"

echo "wp_updater başlatılıyor..."
docker start wp_updater || echo "wp_updater çalıştırılamadı!"

echo "Tüm sistem başarıyla çalıştırıldı!"


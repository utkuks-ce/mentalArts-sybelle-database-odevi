import time
import psycopg2
import pymongo
import redis

DB_HOST = "postgresql"
MONGO_HOST = "mongo"
REDIS_HOST = "redis"

try:
    # PostgreSQL Bağlantısı
    pg_conn = psycopg2.connect(dbname="mydatabase", user="myuser", password="mypassword", host=DB_HOST, port="5432")
    pg_cursor = pg_conn.cursor()
    print("✅ PostgreSQL bağlantısı başarılı!")

    # PostgreSQL Veri Ekleme
    pg_cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100));")
    pg_cursor.execute("INSERT INTO users (name) VALUES ('Utku'), ('Ahmet'), ('Zeynep');")
    pg_conn.commit()
    print("✅ PostgreSQL veri ekleme başarılı!")

    # MongoDB Bağlantısı
    mongo_client = pymongo.MongoClient(f"mongodb://{MONGO_HOST}:27017/")
    mongo_db = mongo_client["mydatabase"]
    mongo_collection = mongo_db["users"]
    print("✅ MongoDB bağlantısı başarılı!")
    mongo_collection.insert_many([{"name": "Utku"}, {"name": "Ahmet"}, {"name": "Zeynep"}])
    print("✅ MongoDB veri ekleme başarılı!")

    # Redis Bağlantısı
    redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
    redis_client.ping()
    print("✅ Redis bağlantısı başarılı!")
    redis_client.set("last_inserted_user", "Zeynep")
    print("✅ Redis veri eklendi!")

    print("🎉 Veri yükleme tamamlandı, çıkılıyor...")
    exit(0)

except Exception as e:
    print(f"⚠️ Hata oluştu: {e}")
    exit(1)


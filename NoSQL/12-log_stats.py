#!/usr/bin/env python3
"""
Nginx loqları haqqında statistika təqdim edən skript
"""
from pymongo import MongoClient


def log_stats():
    """
    MongoDB-dəki loqları analiz edir və çap edir
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # 1. Ümumi loq sayı
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # 2. Metodlar üzrə statistika
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # 3. Status yoxlanışı (method=GET, path=/status)
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    log_stats()

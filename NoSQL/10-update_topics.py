#!/usr/bin/env python3
"""
Bu modul müəyyən bir məktəbin mövzularını (topics) yeniləyir
"""


def update_topics(mongo_collection, name, topics):
    """
    Məktəbin adına əsasən onun mövzular siyahısını yeniləyir
    """
    # update_many(şərt, yeniləmə_əməliyyatı)
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )

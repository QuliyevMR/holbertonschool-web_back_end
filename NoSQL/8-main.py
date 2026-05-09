#!/usr/bin/env python3
"""
Bu modul kolleksiyadakı bütün sənədləri siyahılayır
"""


def list_all(mongo_collection):
    """
    Kolleksiyadakı bütün sənədləri geri qaytarır
    """
    # mongo_collection.find() bütün sənədləri qaytarır
    # Biz onları siyahı (list) formatına salmalıyıq
    return list(mongo_collection.find())

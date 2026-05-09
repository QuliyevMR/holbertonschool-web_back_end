#!/usr/bin/env python3
"""
Bu modul kolleksiyaya yeni sənəd əlavə edir
"""


def insert_school(mongo_collection, **kwargs):
    """
    kwargs daxilindəki məlumatları sənəd kimi bazaya daxil edir
    və yeni yaranan sənədin _id-sini geri qaytarır
    """
    # mongo_collection.insert_one() lüğət (dict) qəbul edir.
    # kwargs özü artıq bir lüğətdir.
    result = mongo_collection.insert_one(kwargs)
    
    # Yeni yaradılan sənədin unikal ID-sini (inserted_id) qaytarırıq
    return result.inserted_id

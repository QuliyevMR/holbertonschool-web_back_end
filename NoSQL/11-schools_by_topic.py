#!/usr/bin/env python3
"""
Bu modul müəyyən bir mövzuya (topic) malik olan məktəblərin siyahısını qaytarır
"""


def schools_by_topic(mongo_collection, topic):
    """
    Göstərilən mövzunu tədris edən məktəblərin siyahısını qaytarır
    """
    # MongoDB avtomatik olaraq "topics" massivinin daxilində
    # bizim verdiyimiz "topic" dəyərini axtaracaq.
    # Nəticəni siyahıya (list) çevirib qaytarırıq.
    return list(mongo_collection.find({ "topics": topic }))

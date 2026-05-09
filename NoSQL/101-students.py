#!/usr/bin/env python3
""" Top students """


def top_students(mongo_collection):
    """
    Tələbələrin ortalama ballarını hesablayır və 
    onları azalan sıra ilə qaytarır.
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "topics": "$topics",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return mongo_collection.aggregate(pipeline)

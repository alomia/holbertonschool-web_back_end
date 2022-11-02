#!/usr/bin/env python3
"""Cache module
"""
import redis
import uuid
from typing import Union


class Cache:
    """This class represents a cache object in redis

    Attributes:

    """
    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """It stores any type of data in redis,
        generates a random key and returns it.

        Args:
            data (str): [STRING]
        """
        key = str(uuid.uuid4())
        self._redis[key] = data
        return key

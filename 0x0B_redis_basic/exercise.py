#!/usr/bin/env python3
"""Cache Module"""

import redis
import uuid


class Cache:
    """This class represents a cache object in redis

    Attributes:

    """
    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    def store(self, data: str) -> str:
        """This method takes a string as an argument, generates a random key,
            stores the input data in Redis using the random key and returns the key.
        Args:
            data (str): [STRING]
        """
        key: str = str(uuid.uuid4())
        self._redis[key] = data
        return key

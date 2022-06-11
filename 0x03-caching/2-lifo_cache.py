#!/usr/bin/env python3
"""2. LIFO Caching"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """represents a LIFO cache system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key key.

        Parameters
        ----------
        key
            key representing a value
        item
            value to assign to a key

        Returns
        -------
        self.cache_data[key] or None
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            key_deleted = list(self.cache_data.keys())[-1]
            del self.cache_data[key_deleted]
            print(f"DISCARD: {key_deleted}")

    def get(self, key):
        """Must return the value in self.cache_data linked to key.

        Parameters
        ----------
        key
            value to look up in the dictionary

        Returns
        -------
        self.cache_data[key] or None
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]

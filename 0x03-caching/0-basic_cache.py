#!/usr/bin/env python3
"""0. Basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents a basic class that generates a cache."""

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

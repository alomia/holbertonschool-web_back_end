#!/usr/bin/env python3
"""5. LFU Caching"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """represents a LFUC cache system"""

    def __init__(self):
        super().__init__()
        self.list_key = []
        self.counter = {}

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
        if not key or not item:
            return
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.list_key:
            self.discard()
        if key not in self.cache_data:
            self.counter[key] = 1
        else:
            self.counter[key] += 1
            self.list_key.remove(key)
        self.list_key.append(key)
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
        self.counter[key] += 1
        self.list_key.remove(key)
        self.list_key.append(key)
        return self.cache_data[key]

    def discard(self):
        """discard item and print

        Parameters
        ----------

        Returns
        -------
        """
        m_time = min(self.counter.values())
        keys = [k for k, v in self.counter.items() if v == m_time]
        low = 0
        while self.list_key[low] not in keys:
            low += 1
        discard = self.list_key.pop(low)
        del self.cache_data[discard]
        del self.counter[discard]
        print(f"DISCARD: {discard}")

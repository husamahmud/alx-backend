#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from base_caching import BaseCaching


class BasicCache (BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key and item:
            self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

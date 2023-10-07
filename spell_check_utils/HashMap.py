class HashMap(dict):
    def __init__(self, *args, **kwargs):
        """
        Initialize a HashMap, which is a custom dictionary that returns an empty list if a key is not found.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        """
        Get the value associated with the given key. If the key is not found, return an empty list and add the key to the dictionary.

        Args:
            key: The key to retrieve the value for.

        Returns:
            Any: The value associated with the key or an empty list if the key is not found.
        """
        if key in self:
            return super().__getitem__(key)
        else:
            super().__setitem__(key, [])  # Initialize the key with an empty list
            return super().__getitem__(key)

    def __setitem__(self, __key, __value):
        __get_value = self.__getitem__(__key)
        __get_value.append(__value)
        __get_value = list(set(__get_value))
        return super().__setitem__(__key, __get_value)
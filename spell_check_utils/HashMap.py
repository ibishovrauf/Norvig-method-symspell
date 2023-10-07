class HashMap(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        else:
            super().__setitem__(key, [])
            return super().__getitem__(key)

class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


print(MyDict({'A': 2, 'B': 6}).get('A'))
print(MyDict({'A': 2, 'B': 6}).get('B'))
print(MyDict({'A': 2, 'B': 6}).get('C'))  # My Dict
print({'A': 2, 'B': 6}.get('C'))  # Default Dict

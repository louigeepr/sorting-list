items = [
    ("Product1", 10),
    ("Product2", 9),
    ("product3", 12),
]


items.sort(key=lambda item: item[1])
print(items)

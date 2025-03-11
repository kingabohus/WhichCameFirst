class Invention:
    def __init__(self, id, name, link, date_text, value_min, value_max, flavor_text):
        self.id = id
        self.name = name
        self.date_text = date_text
        self.value_min = value_min
        self.value_max = value_max
        self.flavor_text = flavor_text
        self.link = link

def compare(invention1, invention2):
    # inv 1 came first
    if invention1.value_max < invention2.value_min:
        return 1
    # inv 2 came first
    elif invention2.value_max < invention1.value_min:
        return 2
    # overlapping dates
    else:
        return 0
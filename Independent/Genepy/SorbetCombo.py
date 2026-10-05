FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

usable = ["Banana",
          "Chocolate",
          "Lemon",
          "Pistachio",
          "Raspberry",
          "Strawberry",
          "Vanilla",]

for i in FLAVORS:
    usable.remove(i)
    for n in usable:
        print(f"{i}, {n}")





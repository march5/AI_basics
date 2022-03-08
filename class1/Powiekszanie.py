napis = "python"
napis = "".join([x.upper() if i % 2 != 0 else x for i, x in enumerate(napis)])
nowyNapis = napis.replace("", " ")
print(nowyNapis)
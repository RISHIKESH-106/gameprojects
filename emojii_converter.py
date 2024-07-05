import demoji
text="I will be your secret santa this year🌋😋😜🤪🤑😛😝"

a=demoji.findall(text)
for keys,values in a.items():
    print(keys, ":", values)
    
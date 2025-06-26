with open("sample.json","w") as file:
    file.write('{"company":"Multicoreware"}')

with open("sample.json","r") as f:
    cont = f.read()
    print(cont)
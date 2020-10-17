import re
f = open("blocklist.xml", "r")
content=f.read()

pattern = re.compile(r'.+[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}.+')  


result=pattern.findall(content)

for i in result:
    print(i)

print(len(result))










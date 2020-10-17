import re
f = open("blocklist.xml", "r")
content=f.read()

pattern = re.compile(r'blockID="i.+\d".+?\n|blockID="g.+\d".+?\n')  


result=pattern.findall(content)

for i in result:
    print(i)




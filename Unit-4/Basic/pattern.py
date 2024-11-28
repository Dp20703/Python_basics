import re
txt='The elephanat is the largest animal of world'
x=re.search('The',txt)
print(re.findall('he',txt))
y=re.split('e',txt)
print(y)
if x:
    print("true")
else:
    print("false")

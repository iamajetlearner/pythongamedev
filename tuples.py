adress=(12,"okg street","london","uk")
print(adress[3])
#adress[3]="UK"
a,b,c,d = adress
#unpacking
print(c)
#check for presence
if "london" in adress:
    print("yes present")
for item in adress:
    print(item)
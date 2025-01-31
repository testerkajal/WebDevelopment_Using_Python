from unicodedata import digit

password = input("Enter the password: ")
result = {}
if len(password) >=8:
    result["length"] = True
else:
    result["length"]=False

digit = False
for i in password:
    i.isdigit()
    digit = True
result["digits"]=digit

upperCase = False
for i in password:
    i.isupper()
    upperCase = True
result["upperCase"]=upperCase

if all(result.values()):
    print("Strong Password")
else:
    print("Weak password")

print(result)



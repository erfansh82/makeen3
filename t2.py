from t1 import d
a=input("do you want to sign in or sign up?")
if a=="sign in":
    us=input("enter your name")
    ps=input("enetr your password")
    if (us,ps) in d.items():
        print("you can sign in welcome....")
else:
    print("you can not sign in....")
print("------------------------------------------------")
if a=="sign up":   
    us1=input("enter your name")
while True:
    ps1=input("enter your password")   
    b=len(ps1)
    if b<=8:
        print("incorect")
        continue
    break
d.update({"us1":"ps1"})
print("you can sign up welcome")






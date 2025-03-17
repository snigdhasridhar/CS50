a=input("greeting:")
a=a.strip()
if ((a[0:5]=="hello" )or (a[0:5]=="Hello")):
    print("$0")
elif((a[0]=="h")or (a[0]=="H")):
    print("$20")
else:
    print("$100")

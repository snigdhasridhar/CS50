a=input("Expression: ")
a=a.strip()
if "+" in a:
    k=a.index("+")
    b=a[0:k]
    c=a[k+1:]
    print(float(b)+float(c))
elif "*" in a:
    k=a.index("*")
    b=a[0:k]
    c=a[k+1:]
    print(float(b)*float(c))
elif "/" in a:
    k=a.index("/")
    b=a[0:k]
    c=a[k+1:]
    print(float(b)/float(c))
elif "-" in a:
    k=a.index("-")
    b=a[0:k]
    c=a[k+1:]
    print(float(b)-float(c))
a=input("File name: ")
a=a.lower().strip()
if ".gif" in a:
    print("image/gif")
elif ".jpg" in a or ".jpeg" in a:
    print("image/jpeg")
elif ".pdf" in a:
    print("application/pdf")
elif ".txt" in a:
    b=a.index(".")
    print("text/"+a[0:b])
elif ".png" in a:
    print("image/png")
elif ".zip" in a:
    print("application/zip")
else:
    print("application/octet-stream")
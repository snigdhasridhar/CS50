def main():
    time=input("What time is it? ")
    convert(time)


def convert(time):
    a=time.index(":")
    hr=int(time[0:a])
    min=int(time[a+1:a+3])
    if "p.m." in time:
        hr=hr+12
    if hr>=7 and hr<=8 and min>=0 and min<=59:
        print("breakfast time")
    elif hr>=12 and hr<=13 and min>=0 and min<=59:
        print("lunch time")
    elif hr>=18 and hr<=19 and min>=0 and min<=59:
        print("dinner time")


if __name__ == "__main__":
    main()

chaukidar=True
while chaukidar:
    rc=int(input("put some numbers here bithc:"))
    r1=0
    r2=1
    bag= f"({r1}{r2})"
    for x in range(0,rc-2):
        r3=r1+r2
        bag=bag+f"{r3}"
        r1=r2
        r2=r3
    print(bag)
    rb=int(input("1 to continue 2 to exit"))

    if rb==2:
        chaukidar=False
        print("ma chudao")


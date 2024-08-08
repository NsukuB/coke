

y=50

x=[5, 10, 25]

while y>0:
    print(f"Amount Due: {y}")
    c=int(input("Insert Coin: "))
    if c in x:
        y-=c

CO=abs(y)

print(f"Change Owed: {CO}")



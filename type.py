def add(a,b):
    if(type(a)==int and type(b)==int):
        return a+b

def sub(a,b):
    if(type(a)==int and type(b)==int):
        return b-a

def main():
    veg=150
    fruits=90
    paid=500
    total = add(veg,fruits)
    getback = sub(total,paid)
    print(getback)

if __name__=="__main__":
    main()

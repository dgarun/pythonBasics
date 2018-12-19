def forloop():
    for num in range(94,109):
        numStr = str(num)
        
        if(len(numStr) ==2):
            print(num/2)
        elif (len(numStr) ==3):
            print(num*2)


def main():
    forloop()

main()

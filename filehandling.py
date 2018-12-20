import sys

#Find argv length and based on length perform the operations

defaultIndex = 1;
startIndex = 1;
endIndex = 1;
if(sys.argv[1] is not None):
    if(sys.argv[1] != ""):
        defaultIndex = sys.argv[1]
    
#if(sys.argv[1] is not None and sys.argv[1] != "" and sys.argv[2] is not None and sys.argv[2] != ""):
  #  startIndex = sys.argv[1];
   # endIndex = sys.argv[2];

print(defaultIndex,startIndex,endIndex)

detailsStr = open(r"details.txt")
#print(detailsStr.readline())

for line in detailsStr:
    #print(line.split(",")[0])
    name = ""
   

#index=0
#while(int(index)<10):
 #   print(detailsStr.readline().split(",")[0])
  #  index = int(index)+1


detailsStr.close()

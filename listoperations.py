orderedList = [1,2,3,4]
reverseOrderedList = orderedList.reverse()

numbers = open("numbers.txt")

#numbersList = numbers.split('\n')
#print(numbers.readline())

numList = []
for number in numbers:
    numList.append(int(number))
    print(int(number))

print(numList)
reversedList = numList.reverse()
sortedList = numList.sort()
print("reversedList - ",reversedList,"|| sortedList - ",sortedList)
numbers.close

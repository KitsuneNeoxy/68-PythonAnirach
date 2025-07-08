numbers = [1, 2 , 3 , 5, 6 , 1 , 3, 4,4,4,4,4] 

dictnum = {}

for number in numbers:
    if number == number:
        dictnum[number] = dictnum.get(number, 0) + 1
    
inverse = [(value,key) for key, value in dictnum.items()]
print(max(inverse)[1])

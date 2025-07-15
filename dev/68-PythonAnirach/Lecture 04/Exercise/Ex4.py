chunk_Size = int(input('Enter chunk: '))
numbers = ""

for i in range(1,101):
    numbers += str(i).rjust(3)

for j in range(0, len(numbers),chunk_Size * 3):
    print(numbers[j:j + chunk_Size * 3]) #J:J เป็นการ slice list


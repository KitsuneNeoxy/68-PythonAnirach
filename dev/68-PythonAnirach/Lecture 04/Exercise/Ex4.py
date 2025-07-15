chunk_Size = int(input('Enter chunk: '))
numbers = ""

for i in range(1,101):
    print(i,end=" ")
    if i % chunk_Size == 0:
        print('')


Total = 0
Time = 0

while True:
    Time += 1
    ItemTwoPointFive = float(input("Enter the item's Wholesale cost: " ))
    Result = ItemTwoPointFive * 2.5
    Total += Result

    print(f'Retail Price : {Result:.2f}')
    print(f'Total Retail Price {Time} Times : {Total:.2f}')
    ContinueChoice = input('Do you have anoter item? (Enter y or Y) for yes: ').lower()

    if ContinueChoice != 'y':
        print('Thank for Using!')
        print('-----------------')
        print(f'Retail Price : {Result:.2f}')
        print(f'Total Retail Price {Time} Times : {Total:.2f}')
        break
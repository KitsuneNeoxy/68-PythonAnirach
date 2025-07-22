from prompt_toolkit.shortcuts import radiolist_dialog

Total = 0
Time = 0

while True:
    Time += 1
    ItemTwoPointFive = float(input("Enter the item's Wholesale cost: "))
    Result = ItemTwoPointFive * 2.5
    Total += Result

    print(f'\nRetail Price : {Result:.2f}')
    print(f'Total Retail Price {Time} Times : {Total:.2f}\n')

    # แทนที่ input ด้วยเมนูเลือก Yes/No แบบลูกศรเลื่อน
    ContinueChoice = radiolist_dialog(
        title="Add More?",
        text="Do you have another item?",
        values=[
            ("y", "Yes"),
            ("n", "No")
        ]
    ).run()

    if ContinueChoice != 'y':
        print('\nThank you for using!')
        print('---------------------')
        print(f'Last Retail Price : {Result:.2f}')
        print(f'Total Retail Price {Time} Times : {Total:.2f}')
        break

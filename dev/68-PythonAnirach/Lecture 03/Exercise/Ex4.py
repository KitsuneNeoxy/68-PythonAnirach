def Add(Numbers1,Numbers2):
    result = Numbers1 + Numbers2
    print(f'{Numbers1} + {Numbers2} = {result}')    

def Subtract(Numbers1,Numbers2):
    result = Numbers1 - Numbers2
    print(f'{Numbers1} - {Numbers2} = {result}')    

def Mutiply(Numbers1,Numbers2):
    result = Numbers1 * Numbers2
    print(f'{Numbers1} × {Numbers2} = {result}')    

def Divide(Numbers1,Numbers2):
    result = Numbers1 / Numbers2
    print(f'{Numbers1} ÷ {Numbers2} = {result}')    

def Selection(Number1,Number2):
    print('Please select Operations - ')
    print('1. Add\n2. Subtract\n3. Multiply\n4. Divide')
    select = int(input('Select Operations form 1, 2, 3, 4: '))
    
    if select == 1:
        Add(Number1,Number2)
    elif select == 2:
        Subtract(Number1,Number2)
    elif select == 3:
        Mutiply(Number1,Number2)
    elif select == 4:
        Divide(Number1,Number2)
    else:
        print('Error! Please Try Against!')
        
    
Number1 = int(input('Enter first number: '))
Number2 = int(input('Enter second number: ')) 

Selection(Number1,Number2)


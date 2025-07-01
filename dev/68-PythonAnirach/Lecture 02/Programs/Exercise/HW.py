Temperature = int(input('Enter temperatures: '))

def TempCalc(Temperature):
    farenheih = (Temperature * 9/5) + 32
    print(f'{farenheih:.2f}')

TempCalc(Temperature)
import time

def displayBMI(bmi_keep):

    print(f'Your BMI is {bmi_keep:.2f}')
    return bmi_keep

def BMI_Calculates(weight,height):
    metersHeight = height / 100
    bmi = weight / (metersHeight * metersHeight)
    displayBMI(bmi)
    

start_time = time.time()

weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in kilometers: '))
BMI_Calculates(weight,height)

end_time = time.time()
print(f'Time taken: {end_time - start_time:.4f} seconds')
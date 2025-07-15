print('KPH''\t''MPH')
print('-----------')

limit_etc = 80

for KPH in range(60,130+1,10):
    MPH = KPH*0.6214
    
    # if KPH <= 80:
    print(f'{KPH}\t{MPH:.1f} ') 
    # elif KPH <= 90: 
    #     print("etc...")
    # elif KPH >= 130:
    #     print(f'{KPH}\t{MPH:.1f} ')
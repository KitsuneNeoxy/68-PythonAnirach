def is_armstrong(numbers):
    number_str = str(numbers)
    length = len(number_str)

    digits = [int(i) for i in number_str]

    total = 0
    for digit in digits:
        total += digit ** length
    
    
    if total == numbers:
        return True
    else: 
        return False
    
    
        

print(is_armstrong(153))
print(is_armstrong(9474))
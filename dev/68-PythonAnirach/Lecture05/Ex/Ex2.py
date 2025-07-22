def generate_prime(n):
    primenum = []
    for i in range(2,n+1):
        divisible = 0
        for j in range(2,i):
            if i % j == 0:
                divisible += 1
                break
        if divisible == 0:
            primenum.append(i)

    print(primenum)

generate_prime(10)
generate_prime(20)
generate_prime(1)
generate_prime(2)
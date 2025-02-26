def prime(n):
    is_prime = False
    for i in range(2,n):
        if n % i == 0:
            return True
    
    return False


if prime(10):
    print("prime")
else:
    print("composite")

    

def prime(n):
    for i in range(2,n//2 + 1):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")            
prime(9)
prime(13)
prime(3)

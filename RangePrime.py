# Printing all prime numbers in range of 1 to 100
lower = 1
upper = 100
print(f"Prime numbers between {lower} and {upper} are:")

for num in range(lower, upper+1):
    #All prime numbers are greater than 1
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if (num % i) == 0:
                break
        else:
            print(num)
        


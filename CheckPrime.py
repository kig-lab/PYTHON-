value = int(input("Enter a number: "))
flag = False

def check_prime(value):
    if value <= 1:
        print(f"{value} is not a prime number.")
    for i in range(2, int(value**0.5)+1):
        if (value % i) == 0:
            print(f"{value} is divisible by {i}, hence it is not a prime number.")
            flag = True
            break
    if flag:
        print(f"{value} is not a prime number.")
    else:
        print(f"{value} is a prime number.")

print(check_prime(value))

insert = int(input("Enter a number: "))
insert2 = int(input("Enter an ending number: "))

def is_prime(number):
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            break
        divisor += 1

    if divisor == number:
        return True
    else:
        return False


def return_primes(maximum):
    list_of_primes = []
    for i in range(2, maximum + 1):
        if is_prime(i):
            list_of_primes.append(i)
 
    print(list_of_primes)


if is_prime(insert):
    print("True")
else:
    print("False")


is_prime(insert)
return_primes(insert2)

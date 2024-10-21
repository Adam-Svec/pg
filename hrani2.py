insert = int(input("Enter a number: "))
insert2 = int(input("Enter the upper limit: "))

def is_prime(number):
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            break
        divisor = divisor + 1

    if divisor == number:
        return True
    else:
        return False


def get_prime_numbers(maximum):
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
get_prime_numbers(insert2)
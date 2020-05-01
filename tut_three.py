#create a list to store the primes
prime_lst = []

#create a funtion that returns true or false in case of a prime
def is_prime(n):
    if n == 1:
        return False #1 is neither a prime or a composite
    
    for i in range(1000, 2000):
        if n % i == 0:
            return False
        return True

#Main function to append list and display the list
if __name__ == '__main__':
    for n in range(1000, 2000):
        if is_prime(n) == True:
            prime_lst.append(n)
            # print(n)
    
    prime_tpl = tuple(prime_lst)
    print(prime_tpl)
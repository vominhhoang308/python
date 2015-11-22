## Name: Minh Hoang VO
## Time:

## Problem 1:

candidate = 1
prime_count = 1
column = 1
nth_prime = 1000
max_column = 10
column_pad = 6

print str(2).center(column_pad),

while prime_count < nth_prime:
    divisor = 2
    prime = 1
    candidate += 2

    while divisor <= candidate**0.5:
        if candidate % divisor == 0:
            prime = 0
            break

        divisor += 1
                
    if prime:
        prime_count += 1

        print str(candidate).center(column_pad),
        column += 1

        if column == max_column:
            print
            column = 0

        if prime_count == nth_prime:
            print ("The 1000th prime is: ", candidate)

        
        

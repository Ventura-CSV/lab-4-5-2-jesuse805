import random

def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    """
    while total <= 100:
        numRan = random.randint(0,100)
        numbers.append(numRan)
        total += numRan
        sum =total - numbers[-1]
    
    """
    ########################################
    """

    print(f'The random values are {numbers}')
    print(f'Total sum of random numbers {sum}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()

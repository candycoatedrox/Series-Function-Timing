from timing import time_function

@time_function
def fib(n):
    'Calculate the fibonnaci numbers using the last two numbers in the sequence.'
    last2 = 0
    last1 = 1
    current = 0

    if n <= 1:
        return 1
    else:
        for i in range(n+1):
            if i > 1:
                current = last2 + last1
                last2 = last1
                last1 = current
            
        return current

def table_fib(n):
    'Tabluate values of the fibonnaci numbers, as well as how long it took to calculate them.'

    print('i\tfib(i)\t\ttime')
    for i in range(n):
        t, r = fib(i)
        print(f'{i}\t{r}\t\t{t}')

def plot_fib(n):
    'Generate a plot showing how long it took to compute the ith fibonnaci number.'
    import matplotlib.pyplot as plt
    times = []
    for i in range(n):
        t, r = fib(i)
        times.append(t)

    plt.plot(times)
    plt.show()

@time_function
def tri(n):
    'Calculate the triangular numbers using the last number in the sequence.'
    tri = 0
    
    if n <= 1:
        return n
    else:
        for i in range(1, n+1):
            tri += i
        return tri


def table_tri(n):
    'Tabluate values of the triangular numbers, as well as how long it took to calculate them.'

    print('i\ttri(i)\t\ttime')
    for i in range(n):
        t, r = tri(i)
        print(f'{i}\t{r}\t\t{t}')

def plot_tri(n):
    'Generate a plot showing how long it took to compute the ith triangular number.'
    import matplotlib.pyplot as plt

    times = []
    for i in range(n):
        t, r = tri(i)
        times.append(t)
    
    plt.plot(times)
    plt.show()

@time_function
def tet(n):
    'Calculate the tetrahedral numbers using the last number in the sequence.'
    tetra = 0
    triN = 0

    if n <= 1:
        return n
    else:
        for i in range(1, n+1):
            _, triN = tri(i)
            tetra += triN
        return tetra

def table_tet(n):
    'Tabluate values of the tetrahedral numbers, as well as how long it took to calculate them.'

    print('i\ttetra(i)\t\ttime')
    for i in range(n):
        t, r = tet(i)
        print(f'{i}\t{r}\t\t{t}')

def plot_tet(n):
    'Generate a plot showing how long it took to compute the ith tetrahedral number.'
    import matplotlib.pyplot as plt

    times = []
    for i in range(n):
        t, r = tet(i)
        times.append(t)
    
    plt.plot(times)
    plt.show()

@time_function
def isPrime(n):
    'Determine whether the number n is prime.'
    prime = True

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3, n//2, 2):
            if n%i == 0:
                prime = False
    
    return prime

def table_prime(n):
    'Tabluate whether a list of numbers up to n are prime, as well as how long it took to calculate them.'

    print('i\tprime?(i)\t\ttime')
    for i in range(n):
        t, r = isPrime(i)
        output = "N"
        if r:
            output = "Y"
        
        print(f'{i}\t{output}\t\t{t}')

def plot_prime(n):
    'Generate a plot showing how long it took to determine whether the ith number in a range is prime.'
    import matplotlib.pyplot as plt

    times = []
    for i in range(n):
        t, r = isPrime(i)
        times.append(t)
    
    plt.plot(times)
    plt.show()


def main():
    table_prime(20)
    plot_prime(20)


if __name__ == '__main__':
    main()
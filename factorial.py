def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
    N = 4
    print(factorial(N))
    #usando il debug, visualizzo lo stack delle chiamate del metodo iterativo
def factorial(n):
    #condizione terminale
    if n == 0 or n == 1:
        return 1
    #condizione non terminale
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    N = 20
    print(factorial(N))
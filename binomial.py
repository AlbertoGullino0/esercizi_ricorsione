
def binomial(n,m):
    #terminale
    if m==0 or m==n:
        return 1
    # non terminale
    else:
        return (binomial(n-1,m-1) +
                binomial(n-1,m))
    #non dobbiamo cercare soluzione complessa, dobbiamo pensare più semplice possibile e la funzione raggiungerà il risultato
if __name__ == '__main__':
    n = 6
    m = 3
    print(binomial(n,m))
        # usando il debug, visualizzo lo stack delle chiamate del metodo iterativo
def binomial(n, m):
    # terminale
    if m == 0 or m == n:
        return 1
    # non terminale
    else:
        return (binomial(n-1, m-1) +
                binomial(n-1, m))


if __name__ == '__main__':
    n = 6
    m = 3
    print(binomial(n, m))
input("press Enter to start...");
def isPrime(n):
    if n < 2:
        return False;
    for i in range(2, n // 2 + 1):
        if (n % i) == 0:
            return False;
    return True;
def p_primes():
    z = int(input(" n = ? "));
    n, x, i = 1, 2, 1;
    pseudoprimes, notpseudoprimes, primes= [], [], [];
    while x >= n:
        while n <= z :
            result = x ** (n - 1);
            if (result % n == 1):
                pseudoprimes.append(n);
            else:
                notpseudoprimes.append(n);
            n +=1;
        x += 1;
    notpseudoprimes.remove(2)
    for k in range(n + 1):
        if isPrime(k):
            primes.append(k);
            if k in pseudoprimes:
                pseudoprimes.remove(k);
    print("\n\n These are pseudoprimes \n\n", pseudoprimes,"\n\n\n These are primes \n\n", primes, "\n\n\n And these are not pseudoprimes nor primes \n\n", notpseudoprimes);
p_primes();
input("\n press Enter to close...");

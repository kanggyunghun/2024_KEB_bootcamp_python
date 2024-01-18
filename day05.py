n1, n2 = map(int,input('enter number :').split().sort())
n1, n2 = min(n1, n2), max(n1, n2)

for number in range(n1, n2 + 1):
    is_prime = True

    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')
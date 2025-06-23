def sqrt1(x, initial_guess=1.0,delta=0.001):
    a = initial_guess

    i = 0
    a = 0.5 * (a + (x/a)) 
    saved = a+1.0
    while abs(saved-a) > delta:
        saved = a
        a = 0.5 * (a + (x/a)) 
        print('Iteration', ' ', i, ':', ' ', a, sep='')
        i += 1
    return a

n=float(input("\nCompute square root of: "))
a=float(input("Enter the initial guess: "))

print("\nComputing the square root of", n, "numerically and interatively.\n")
s = sqrt1(n,a)

print("\nThe square root of", n, "is:", s)

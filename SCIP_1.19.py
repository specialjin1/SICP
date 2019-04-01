def fib(n):
    def even(number):
        return number%2==0

    def square(number):
        return number*number

    def fib_iter(a, b, p, q, count):
        if count==0:
            return b
        elif even(count)==0:
            print(a, ' ', b, ' ', p*p+q*q, ' ', q*q+2*p*q, ' ', int(count/2))
            return fib_iter(a, b, p*p+q*q, q*q+2*p*q, int(count/2))
        else:
            print(b*q+a*q+a*p, ' ', b*p+a*q, ' ', p, ' ', q, ' ', count-1)
            return fib_iter(b*q+a*q+a*p, b*p+a*q, p, q, count-1)

    fib_iter(1,0,0,1,n)

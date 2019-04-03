def fib(n):
    def even(number):
        return number%2==0

    def square(number):
        return number*number

    def fib_iter(a, b, p, q, count):
        if count==0:
            return b
        elif even(count):
            return fib_iter(a, b, square(p)+square(q), square(q)+2*p*q, int(count/2))
        else:
            return fib_iter(b*q+a*q+a*p, b*p+a*q, p, q, count-1)

    print(fib_iter(1,0,0,1,n))

fib(1)
fib(2)
fib(3)
fib(4)
fib(5)
fib(6)
fib(7)
fib(8)
fib(9)
fib(10)
fib(11)
fib(12)

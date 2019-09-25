#what is a Fibonacci numbers

# what is an order of mangnatude

#given an input number N, write a function to compute the Nth fibonacci number

fib_list = [0,1]

def fibonacci(N):
    if N < 0:
        return "N cannot be less than 0"

    elif N <=1:
        return 1

    else:
        for i in range(2, N+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[N]
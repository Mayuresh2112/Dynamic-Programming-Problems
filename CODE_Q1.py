def fibonacci(n):
    r=[-1]*(n+1)
    return fibonacci_helper(n,r)
def fibonacci_helper(n,r):
    if r[n]>=0:
        return r[n]
    if n==0 or n==1:
        q=n
    else:
        q=fibonacci_helper(n-1,r)+fibonacci_helper(n-2,r)
    r[n]=q
    return q


x= int(input("Enter nth Element to find Fibonacci Number through DP Memoization:- "))
print(fibonacci(x))
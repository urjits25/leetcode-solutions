'''

POW(X,N)

Implement pow(x, n), which calculates x raised to the power n (xn).

'''

def myPow(x: float, n: int) -> float:
    if n < 0:
        x, n = (1/x), -n
    if n == 0: 
        return 1
        
    if n % 2:
        return x * self.myPow(x*x, n//2)
    return self.myPow(x*x, n//2) 

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1
 
# Calculate Fn mod m
def fibonacciModulo(n, m):
     
    # Getting the period
    pisano_period = pisanoPeriod(m)
     
    # Taking mod of N with
    # period length
    n = n % pisano_period
     
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current \
        = current, previous + current
         
    return (current % m)
 
# Driver Code
if __name__ == '__main__':
    n = 1548276540
    m = 4
    print(pisanoPeriod(m))
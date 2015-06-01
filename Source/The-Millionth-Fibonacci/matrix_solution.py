'''
this is a algorithm based on Matrix.
in fibonacci sequence, we can define a Matrix of 2*2 as [[fib(n+1),fib(n)][fib(n),fib(n-1)]]
it is easy to show that this Matrix is the result of [[fib(n),fib(n-1)][fib(n-1),fib(n-2)]]*[[1,1],[1,0]]

in function mul we define the multiply operation of two matrix in [[a,b][b,c]] format.
in function pow_matrix we define the power operation via recursion

I found this algorithm on http://en.literateprograms.org/Fibonacci_numbers_(Python)
'''

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a * d + b * e, a * e + b * f, b * e + c * f


def pow_matrix(A, n):
    if n == 1: return A
    if n &1 == 0: return pow_matrix(mul(A, A), n // 2)
    return mul(A, pow_matrix(mul(A, A), (n - 1)//2))


def fib(n):
    if n<0 :
        return fib(-n) if not n%2 == 0 else -fib(-n)
    if n < 2: return n
    return pow_matrix((1, 1, 0), n - 1)[0]

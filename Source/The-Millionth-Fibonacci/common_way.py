'''
A solution based on the defination of Fibonacci sequence using recursion.
When n reaches a large number, this solution can be quite slow.
'''


def fib(n):
  if n < 2: return n
  return fib(n-1)+fib(n-2)
  
  
'''
A solution based on the defination of Fibonacci sequence using list.
It's faster than the solution above, but still not fast enough.

BTW, this is my first solution to this Kata, but it didn't pass the efficiency test.
'''


def fib(n):
  l = [0,1]
  if n < len(l)-1: return l[n]
  while len(l)<n :
    l.append(l[len(l)-1]+l[len(l)-2])
  return l(n)

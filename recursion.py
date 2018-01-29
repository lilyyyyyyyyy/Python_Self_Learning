
import sys

def factorial(n):
  if n == 0:
    return(1)
  else: return( n * factorial(n-1))
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)

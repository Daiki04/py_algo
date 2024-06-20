import sys
import time
sys.setrecursionlimit(10**6)
def power(n, m):
    if m == 0:
        return 1
    else:
        return n * power(n, m-1)

if __name__ == '__main__':
    start_t = time.time()

    print(power(2, 10000))
    print(time.time() - start_t)
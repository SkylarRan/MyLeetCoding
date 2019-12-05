def squareRoot(n):
    if n < 0:
        return -1
    
    if n == 0:
        return 0


    low = 0
    high = n
    mid = n / 2
    while abs(mid ** 2 - n) > 0.000001:
        if mid ** 2 > n:
            high = mid
        else
    return i


if __name__ == '__main__':
    print(squareRoot(9))



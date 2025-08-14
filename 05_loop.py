#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i²

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if i < n:
            print(i**2)
        else:
            print()
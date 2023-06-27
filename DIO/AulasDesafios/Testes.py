T = int(input())
for i in range(T):
    n, k = map(int, input().split())
    result = (n % k) + (n / k)
    print(f'{int(result)}')

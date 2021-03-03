#92p 큰 수의 법칙
# N = 5, M = 8, K = 3
#2 4 5 4 6

n,m,k = map(int,input().split())
data = list(map(int, input().split()))
data = sorted(data)

Max1 = data[n-1]
print(Max1)
Max2 = data[n-2]
print(Max2)
result = Max1 * (k * (m // k)) + Max2 * (m-(k * (m // k))) # 첫 번째로 큰 Max1 더하는 횟수 + 두 번째로 큰 Max2 더하는 횟수
print(result)



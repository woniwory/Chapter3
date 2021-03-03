#99p 1이 될 때 까지

n,k = map(int,input().split())
count = 0

while n >= k:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)
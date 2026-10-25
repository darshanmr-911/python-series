from collections import Counter
# Input
n = int(input())
chocolates = list(map(int, input().split()))
m = int(input())
# Count available chocolates
choco_count = Counter(chocolates)
total_earnings = 0
for _ in range(m):
    desired, price = map(int, input().split())    
    if choco_count[desired] > 0:
        total_earnings += price
        choco_count[desired] -= 1
print(total_earnings)